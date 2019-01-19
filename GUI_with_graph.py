#!/usr/bin/python3

# default
import sys
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

# from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import QPoint, Qt, QTime, QTimer
#from PyQt5.QtGui import QPalette

# from PyQt5.QtWidgets import QApplication, QPushButton

from PyQt5.QtWidgets import *
"""from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QMessageBox, QDesktopWidget, QApplication, QVBoxLayout, QLabel)
"""
#from PyQt5.QtGui import QIcon
#from PyQt5.QtGui import QFont

#
import random

# for update

# file = "/home/pi/projectScreen/cpu_temp.csv"
file = "cpu_temp.csv"
# for file and temp
# from gpiozero import CPUTemperature


# global var
# cpu = CPUTemperature()

class TheMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(TheMainWindow, self).__init__(parent)

        self.main_widget = QWidget(self)

        self.graph_widget = GraphWindow(self)
        self.setCentralWidget(self.graph_widget)


class ClockWindow():
    def __init__(self, parent=None):
        return super().__init__(parent)
        self.clock()

    def clock(self):
        pass

    def updateClock(self):
        time = strftime("%Y-%m-%d %H:%M:%S")
        label = QLabel(time)


class GraphWindow(QWidget):
    def __init__(self, parent=None):
        super(GraphWindow, self).__init__(parent)

        timer = QTimer(self)
        timer.timeout.connect(self.plotLive)
        timer.start(10000)

        # a figure instance to plot on
        #self.clockFigure = plt.figure()
        self.figure = plt.figure()
        self.figure2 = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        #self.clockCanvas = FigureCanvas(self.clockFigure)
        self.canvas = FigureCanvas(self.figure)
        self.canvas2 = FigureCanvas(self.figure2)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        #self.clockToolbar = NavigationToolbar(self.clockCanvas, self)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)

        # button connected to `plot` method
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)
        #self.button2 = QPushButton('Plot2')
        # self.button2.clicked.connect(self.plotLive)

        # set the layout
        layout = QVBoxLayout()

        self.label = QLabel("My text")
        # layout.addWidget(self.clock)
        layout.addWidget(self.label)

        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        # layout.addWidget(self.toolbar2)
        layout.addWidget(self.canvas2)
        # layout.addWidget(self.button2)
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

        # get and set data to plot
        append_to_file()
        xs, ys = read_from_file()

        # plot data
        ax1.scatter(xs, ys)
        ax1.plot(xs, ys)

        # refresh canvas
        self.canvas2.draw()


def read_from_file():
    # open file and append it to array
    graph_data = open(file, 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(float(y))

    return xs, ys


def append_to_file():
    # temp = cpu.temperature
    temp = 45
    with open(file, "a") as log:
        log.write("{},{}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp)))


# def get_cpu_temp():
#    return cpu.temperature


if __name__ == '__main__':
    app = QApplication(sys.argv)

    #main = Window()
    # main.show()
    main = TheMainWindow()
    main.show()

    sys.exit(app.exec_())
