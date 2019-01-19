import sys
from piDisplayGUI import Ui_MainWindow

# from PyQt5 import QtCore
# from PyQt5.QtCore import QPoint, Qt, QTime, QTimer
# from PyQt5.QtGui import QPalette

from PyQt5.QtWidgets import *

# from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5 import QtWidgets


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtGui.QMainWindow.__init__(self)

        self.ui.setupUi(self)
        self.setupUi(self)
        self.show()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.handle_update_time())
        timer.start(1000)

    def setupUi(self, MainWindow):
        return super().setupUi(MainWindow)

        # self.pushButton.pressed.connect(self.update_weather)

        # self.threadpool = QThreadPool()

    def handle_b_update(self):
        self.update_clicked()

    def handle_b_update_2(self):
        self.update_clicked_2()

    def update_clicked(self):
        # code for button clicked
        print("button update clicked")
        self.label.setText(str(get_cpu_temp()) + "*C")

    def update_clicked_2(self):
        # code for button clicked
        print("button update clicked 2")
        self.label_2.setText(str(get_temp()) + "*C")

    def handle_update_time(self):
        self.update_time()

    def update_time(self):
        self.lcdNumber.setDecMode()
        self.lcdNumber.Dec(12)


def get_cpu_temp():
    # return cpu.temperature
    return 46


def get_temp():
    return 21


def get_time():
    return "10:30"


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
