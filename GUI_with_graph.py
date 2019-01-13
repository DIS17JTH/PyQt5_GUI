#!/usr/bin/python3

# default
import sys
import math
# import numpy as np
# import time
from time import sleep, strftime, time

# matplotlib
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

# PyQt5

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
# from PyQt5.QtWidgets import QApplication, QPushButton

from PyQt5.QtWidgets import *
"""from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QMessageBox, QDesktopWidget, QApplication, QVBoxLayout, QLabel)
"""
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont

import random


# for file and temp
from gpiozero import CPUTemperature
#file = '/home/pi/PyQt5_GUI/PyQt5_GUI/cpu_temp.csv'
file = 'cpu_temp.csv'
# global var
cpu = CPUTemperature()


def read_from_file():
    # open file and append it to array
    myfile = open(file, 'r')
    graph_data = myfile.read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(float(y))
    myfile.close()
    return xs, ys


def append_to_file(temp):  # write temp to file
    with open(file, "a") as log:
        log.write("{},{}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp)))
    log.close()


class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()
        self.figure2 = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas2 = FigureCanvas(self.figure2)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)

        # Just some button connected to `plot` method
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        self.button2 = QPushButton('Plot2')
        self.button2.clicked.connect(self.plotLive)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        layout.addWidget(self.toolbar2)
        layout.addWidget(self.canvas2)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random() for i in range(10)]

        # instead of ax.hold(False)
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        # ax.hold(False) # deprecated, see above

        # plot data
        ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()

    def plotLive(self):

        # instead of ax.hold(False)
        self.figure2.clear()

        # create an axis
        # self refers to a figure
        ax1 = self.figure2.add_subplot(1, 1, 1)

        # discards the old graph
        # ax.hold(False) # deprecated, see above

        ax1.clear()
        # plt.clf()

        # plot data
        temp = cpu.temperature
        append_to_file(temp=temp)
        xs, ys = read_from_file()

        ax1.scatter(xs, ys)
        ax1.plot(xs, ys)

        # refresh canvas
        self.canvas2.draw()


"""
def get_cpu_temp():
    return cpu.temperature
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
