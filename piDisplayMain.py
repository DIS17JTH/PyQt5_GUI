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
from PyQt5.QtCore import QTimer

# for pi cpu temp
from gpiozero import CPUTemperature
cpu = CPUTemperature()


class MainWindow(QMainWindow, Ui_MainWindow):
    def pressed_b_update(self):
        print("Pressed btn update")

    def pressed_b_update_2(self):
        print("Pressed btn update 2")

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # hooks for btn:s
        self.b_update.clicked.connect(lambda: self.pressed_b_update())
        self.b_update_2.clicked.connect(lambda: self.pressed_b_update_2())

        self.lcdNumber.display("00:00")

        timer_clock = QTimer(self)
        timer_clock.timeout.connect(self.update_time)
        timer_clock.setInterval(1000)
        timer_clock.start()

        temp = get_temp()
        cpu_temp = get_cpu_temp()

        self.label.setText(str(temp) + '°' + 'C')
        self.label_2.setText(str(cpu_temp) + '°' + 'C')

        timer_temp = QTimer(self)
        timer_temp.timeout.connect(self.update_temp)
        timer_temp.setInterval(10000)
        timer_temp.start()

    """
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        self.setupUi(self)
        Ui_MainWindow.__init__(self)

        # hooks
        self.b_update.clicked.connect(lambda: self.handle_b_update)

        # QtGui.QMainWindow.__init__(self)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        # self.setupUi(self)

        # self.ui.b_update.setText("Text")

        # self.ui.label_2.setText("Label_2_edited")

        # not Working
        """
    # timer = QtCore.QTimer(self)
    # timer.timeout.connect(self, self.handle_update_time())
    # timer.start(1000)
    """

        # continue to try: access buttons in UI file
        # self.b_update.clicked.connect(self.handle_b_update)
        # self.b_update.pressed.connect(self.handle_b_update)
        # self.b_update_2.pressed.connect(self.handle_b_update_2)

        self.show()
    """

    def update_clicked(self):
        # code for button clicked
        print("button update clicked")
        self.label.setText(str(get_cpu_temp()) + '°' + 'C')

    def update_clicked_2(self):
        # code for button clicked
        print("button update clicked 2")
        self.label_2.setText(str(get_temp()) + '°' + 'C')

    def handle_update_time(self):
        self.update_time()

    def update_time(self):
        # self.lcdNumber.setDecMode()
        # self.lcdNumber.Dec(12)
        print("update time")
        self.lcdNumber.display(strftime("%H:%M"))

    def update_temp(self):
        print("update temp °C")
        temp = get_temp()
        cpu_temp = get_cpu_temp()
        # print(temp)
        # print(cpu_temp)
        self.label.setText(str(temp) + '°' + 'C')
        self.label_2.setText(str(cpu_temp) + '°' + 'C')

    def setupUi(self, MainWindow):
        return super().setupUi(MainWindow)

        # self.pushButton.pressed.connect(self.update_weather)


def get_cpu_temp():
    # temp = 46
    temp = cpu.temperature
    return temp


def get_temp():
    return 21


def get_time():
    return "10:30"


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # mainWindow = QtWidgets.QMainWindow()
    mainWindow = MainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(mainWindow)

    # ui.b_update_2.setText("set text")

    mainWindow.show()
    sys.exit(app.exec_())
