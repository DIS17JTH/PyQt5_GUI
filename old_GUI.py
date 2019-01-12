#!/usr/bin/python3

# default
import sys
#import numpy as np
import time
import itertools

# matplotlib
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# PyQt5

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
#from PyQt5.QtWidgets import QApplication, QPushButton

from PyQt5.QtWidgets import *
"""from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QMessageBox, QDesktopWidget, QApplication, QVBoxLayout, QLabel)
"""
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont


app = QApplication([])
app.setStyle('Fusion')
#app.setStyleSheet("QPushButton { margin: 1ex; } QLabel { margin: 2ex; }")
app.setStyleSheet("QLabel { margin: 4ex; }")

window = QWidget()

layout = QVBoxLayout()

label = QLabel('Hello World!')
layout.addWidget(label)

layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))

palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)
button = QPushButton('Hello World')
layout.addWidget(button)

button = QPushButton('Click')


def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()


button.clicked.connect(on_button_clicked)
layout.addWidget(button)


window.setLayout(layout)

fig = plt.figure(1, (10, 10))
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    graph_data = open('cpu_temp.csv', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(float(y))
    ax1.clear()
    # plt.clf()
    ax1.scatter(xs, ys)
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=10000)
plt.show()


window.show()
app.exec_()
