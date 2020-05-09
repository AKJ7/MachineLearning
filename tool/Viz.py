import matplotlib.pyplot as plt
import numpy as np
from typing import *
import time

__all__ = [
    'IterationVisualizer2D',
    'IterationVisualizer3D'
]


class IterationVisualizer2D:
    def __init__(self, start, end, num, delay: int):
        self.__delay = delay
        fig, self.__figure = plt.subplots()
        self.x = np.linspace(start, end, num)

    def plot(self, func, label=''):
        self.__figure.plot(self.x, func, label)
        plt.pause(self.__delay)

    def point(self, x, y):
        self.__figure.plot(x, y, '-ro')
        plt.pause(self.__delay)


class IterationVisualizer3D:
    def __init__(self, startX, endX, numX, startY, endY, numY, delay):
        self.__delay = delay
        self.__fig = plt.figure(figsize=plt.figaspect(2.))
        self._plot = self.__fig.add_subplot(1, 1, 1, projection='3d')
        self._X = np.arange(startX, endX, numX)
        self._Y = np.arange(startY, endY, numY)
        self._X, self._Y = np.meshgrid(self._X, self._Y)

    def plot(self, func):
        self._plot.plot_surface(self._X, self._Y, func(self._X, self._Y))
        plt.pause(self.__delay)

    def add_point(self, x, y, z):
        self._plot.scatter(x, y, z, c='red', depthshade=False)
        plt.pause(self.__delay)

# IT = IterationVisualizer([[-10, 10], [-20, 2]], 100, 2)
# fig = plt.figure(figsize=plt.figaspect(2.))
# b = fig.add_subplot(2, 1, 2, projection='3d')
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# Z = 0.5 * (X**2) + 2.5 * (Y**2)
# b.plot_surface(X, Y, Z)
#


# m = IterationVisualizer3D(-5, 5, 0.25, -5, 5, 0.25, 2)
# m.plot(lambda x, y: 0.5 * (x**2) + 2.5 * (y**2))
# m.add_point(0, 0, 0)
