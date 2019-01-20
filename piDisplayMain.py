import sys
from piDisplayGUI import Ui_MainWindow
from time import sleep, strftime, time

# from PyQt5 import QtCore
# from PyQt5.QtCore import QPoint, Qt, QTime, QTimer
# from PyQt5.QtGui import QPalette

from PyQt5.QtWidgets import *

# from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5 import QtWidgets
from PyQt5 import QtCore


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        # QtGui.QMainWindow.__init__(self)

        Ui_MainWindow.__init__(self)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.setupUi(self)

        # self.ui.b_update.setText("Text")

        # self.ui.label_2.setText("Label_2_edited")

        # not Working
        """
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self, self.handle_update_time())
        timer.start(1000)
        """

        # continue to try: access buttons in UI file
        # self.b_update.clicked.connect(self.handle_b_update)
        # self.b_update.pressed.connect(self.handle_b_update)
        # self.b_update_2.pressed.connect(self.handle_b_update_2)

        self.show()

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
        # self.lcdNumber.setDecMode()
        # self.lcdNumber.Dec(12)
        print("update time")

    def setupUi(self, MainWindow):
        return super().setupUi(MainWindow)

        # self.pushButton.pressed.connect(self.update_weather)


def get_cpu_temp():
    # return cpu.temperature
    return 46


def get_temp():
    return 21


def get_time():
    return "10:30"


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    #MainWindow = QtWidgets.QMainWindow()
    mainWindow = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)

    #ui.b_update_2.setText("set text")

    mainWindow.show()
    sys.exit(app.exec_())
