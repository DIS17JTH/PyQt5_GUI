# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piDisplayGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

# clock inports
from time import sleep, strftime, time
from PyQt5.QtCore import QTimer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(790, 470))
        self.centralwidget.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.centralwidget.setTabletTracking(True)
        self.centralwidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.centralwidget.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.Sweden))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 50, 541, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_main = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_main.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_main.setObjectName("gridLayout_main")
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_main.addWidget(self.line_2, 1, 0, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_main.addWidget(self.lcdNumber, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_main.addWidget(self.line, 1, 1, 1, 1)
        self.horizontalLayout_top_right = QtWidgets.QHBoxLayout()
        self.horizontalLayout_top_right.setObjectName(
            "horizontalLayout_top_right")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("font: 18pt \"Myanmar Text\";")
        self.label.setObjectName("label")
        self.horizontalLayout_top_right.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("font: 18pt \"Myanmar Text\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_top_right.addWidget(self.label_2)
        self.gridLayout_main.addLayout(
            self.horizontalLayout_top_right, 0, 1, 1, 1)
        self.tabWidget_bottom_left = QtWidgets.QTabWidget(
            self.gridLayoutWidget)
        self.tabWidget_bottom_left.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget_bottom_left.setObjectName("tabWidget_bottom_left")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(2, 6, 311, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_weather = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_weather.setObjectName("widget_weather")
        self.verticalLayout.addWidget(self.widget_weather)
        self.lineEdit_location = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_location.setObjectName("lineEdit_location")
        self.verticalLayout.addWidget(self.lineEdit_location)
        self.b_update = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.b_update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_update.setObjectName("b_update")
        self.verticalLayout.addWidget(self.b_update)
        self.tabWidget_bottom_left.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 321, 221))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_plotRandom = QtWidgets.QWidget(self.verticalLayoutWidget_3)
        self.widget_plotRandom.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.widget_plotRandom.setObjectName("widget_plotRandom")
        self.verticalLayout_4.addWidget(self.widget_plotRandom)
        self.b_update_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.b_update_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_update_2.setObjectName("b_update_2")
        self.verticalLayout_4.addWidget(self.b_update_2)
        self.tabWidget_bottom_left.addTab(self.tab_2, "")
        self.gridLayout_main.addWidget(self.tabWidget_bottom_left, 2, 0, 1, 1)
        self.verticalLayout_bottom_right = QtWidgets.QVBoxLayout()
        self.verticalLayout_bottom_right.setObjectName(
            "verticalLayout_bottom_right")
        self.widget_plotLive = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_plotLive.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.widget_plotLive.setObjectName("widget_plotLive")
        self.verticalLayout_bottom_right.addWidget(self.widget_plotLive)
        self.gridLayout_main.addLayout(
            self.verticalLayout_bottom_right, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGeneral = QtWidgets.QAction(MainWindow)
        self.actionGeneral.setObjectName("actionGeneral")
        self.actionVersion_1_0 = QtWidgets.QAction(MainWindow)
        self.actionVersion_1_0.setObjectName("actionVersion_1_0")
        self.actionLanguage = QtWidgets.QAction(MainWindow)
        self.actionLanguage.setObjectName("actionLanguage")
        self.actionSize = QtWidgets.QAction(MainWindow)
        self.actionSize.setObjectName("actionSize")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuOptions.addAction(self.actionGeneral)
        self.menuOptions.addAction(self.actionLanguage)
        self.menuOptions.addAction(self.actionSize)
        self.menuAbout.addAction(self.actionVersion_1_0)
        self.menuWindow.addAction(self.actionQuit)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_bottom_left.setCurrentIndex(1)
        self.b_update.clicked.connect(self.handle_b_update)
        self.b_update_2.clicked.connect(self.handle_b_update_2)

        self.lineEdit_location.textChanged['QString'].connect(
            self.label_2.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        """
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.handle_update_time())
        timer.start(1000)
        """

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.b_update.setText(_translate("MainWindow", "Update"))
        self.tabWidget_bottom_left.setTabText(self.tabWidget_bottom_left.indexOf(
            self.tab), _translate("MainWindow", "Tab 1"))
        self.b_update_2.setText(_translate("MainWindow", "update"))
        self.tabWidget_bottom_left.setTabText(self.tabWidget_bottom_left.indexOf(
            self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionGeneral.setText(_translate("MainWindow", "General"))
        self.actionVersion_1_0.setText(_translate("MainWindow", "Version 1.0"))
        self.actionLanguage.setText(_translate("MainWindow", "Language"))
        self.actionSize.setText(_translate("MainWindow", "Size"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


def get_cpu_temp():
    # return cpu.temperature
    return 46


def get_temp():
    return 21


def get_time():
    return "10:30"


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
