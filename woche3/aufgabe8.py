import numpy as np
import matplotlib.pyplot as plt


def calculate_cost_value(w):
    # return np.log(1 + np.exp(w * w))
    return w ** 4 + w ** 2 + 10 * w


def calculate_gradient(w):
    # return 2*w*np.exp(w**2)*(1 / (1 + np.exp(w**2)))
    return 4 * (w ** 3) + 2 * w + 10


def surrogate(y, x):
    g = calculate_cost_value(y)
    grad = calculate_gradient(y)
    return g + grad * (x - y)


def make_function(ax):
    # Wiederholung der Konvexe Funktion mit calculate_cost_value ersetzt (Zeile 51)
    s = np.linspace(-3, 2, 200)
    t = calculate_cost_value(s)
    ax.plot(s, t, '-k', linewidth=2)
    ax.set_xlim(-3, 2)
    ax.set_ylim(-30, 60)
    ax.set_xlabel('$w$', fontsize=20, labelpad=20)
    ax.set_ylabel('$g(w)$', fontsize=20, rotation=0, labelpad=20)


def plot_steps_with_surrogate(w_path):
    fig = plt.figure(facecolor='white')
    ax1 = fig.add_subplot(111)
    assert len(w_path) > 0
    # For loop durch Funktionaufruf ersetzt
    g_path = calculate_cost_value(w_path)
    make_function(ax1)
    # Farbereihenfolgeaenderung: Frueher Rot -> Gruen, jetzt umgekehr
    s = np.linspace(1, 1 / len(g_path), len(g_path))
    s.shape = (len(s), 1)
    # Zusammenfasssung und s.shape statt len(s), 1
    colorspec = np.concatenate((s, np.flipud(s), np.zeros(s.shape)), 1)
    s = np.linspace(-3, 2, 200)
    for zaehler in range(len(w_path)):
        ax1.plot(w_path[zaehler], g_path[zaehler], 'o', markersize=10, color=colorspec[zaehler], markerfacecolor=colorspec[zaehler])
        if zaehler < 4:
            ax1.plot(s, surrogate(w_path[zaehler], s), color=colorspec[zaehler])
        plt.pause(0.5)
    # Alles anderes weg !!!


def gradientenVerfahren(nabla_f, schrittweite, startpunkt):
    zaehler = 1
    ret = []
    while zaehler < 50:
        startpunkt = startpunkt - schrittweite * nabla_f(startpunkt)
        zaehler += 1
        ret.append(startpunkt)
    return np.array(ret)


plot_steps_with_surrogate(gradientenVerfahren(calculate_gradient, 0.15, -1))
