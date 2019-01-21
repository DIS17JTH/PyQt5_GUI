import sys
from piDisplayGUI_v2 import Ui_MainWindow
from time import sleep, strftime, time

# from PyQt5 import QtCore
# from PyQt5.QtCore import QPoint, Qt, QTime, QTimer
# from PyQt5.QtGui import QPalette

#from PyQt5.QtWidgets import *

# from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QFont
#from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer

# weather imports
from datetime import datetime
import json
import os
import sys
import requests
from urllib.parse import urlencode
#from PyQt5.QtCore import QObject
#from PyQt5.QtCore import (Qt, pyqtSignal)
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# for pi cpu temp
from gpiozero import CPUTemperature
cpu = CPUTemperature()


OPENWEATHERMAP_API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')


def from_ts_to_time_of_day(ts):
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%I%p").lstrip("0")


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.
    '''
    finished = pyqtSignal()
    error = pyqtSignal(str)
    result = pyqtSignal(dict, dict)


class WeatherWorker(QRunnable):
    '''
    Worker thread for weather updates.
    '''
    signals = WorkerSignals()
    is_interrupted = False

    def __init__(self, location):
        super(WeatherWorker, self).__init__()
        self.location = location

    @pyqtSlot()
    def run(self):
        try:
            params = dict(
                q=self.location,
                appid=OPENWEATHERMAP_API_KEY
            )

            url = 'http://api.openweathermap.org/data/2.5/weather?%s&units=metric' % urlencode(
                params)
            r = requests.get(url)
            weather = json.loads(r.text)

            # Check if we had a failure (the forecast will fail in the same way).
            if weather['cod'] != 200:
                raise Exception(weather['message'])

            url = 'http://api.openweathermap.org/data/2.5/forecast?%s&units=metric' % urlencode(
                params)
            r = requests.get(url)
            forecast = json.loads(r.text)

            self.signals.result.emit(weather, forecast)

        except Exception as e:
            self.signals.error.emit(str(e))

        self.signals.finished.emit()


class MainWindow(QMainWindow, Ui_MainWindow):
    def pressed_b_update(self):
        print("Pressed btn update")

    def pressed_b_update_2(self):
        print("Pressed btn update 2")

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        # hooks for btn:s
        #self.b_update.clicked.connect(lambda: self.pressed_b_update())
        self.b_update_2.clicked.connect(lambda: self.pressed_b_update_2())

        #timers#
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
        #end timers#

        #weather#
        self.b_update.pressed.connect(self.update_weather)

        self.threadpool = QThreadPool()
        #end weather#

        # self.show()

    # basic
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
    # end basic

    # weather
    def alert(self, message):
        alert = QMessageBox.warning(self, "Warning", message)

    def update_weather(self):
        worker = WeatherWorker(self.lineEdit_location.text())
        worker.signals.result.connect(self.weather_result)
        worker.signals.error.connect(self.alert)
        self.threadpool.start(worker)

    def weather_result(self, weather, forecasts):  # not implemented
        self.latitudeLabel.setText("%.2f °" % weather['coord']['lat'])
        self.longitudeLabel.setText("%.2f °" % weather['coord']['lon'])

        self.windLabel.setText("%.2f m/s" % weather['wind']['speed'])

        self.temperatureLabel.setText("%.1f °C" % weather['main']['temp'])
        self.pressureLabel.setText("%d" % weather['main']['pressure'])
        self.humidityLabel.setText("%d" % weather['main']['humidity'])

        self.sunriseLabel.setText(
            from_ts_to_time_of_day(weather['sys']['sunrise']))

        self.weatherLabel.setText("%s (%s)" % (
            weather['weather'][0]['main'],
            weather['weather'][0]['description']
        )
        )

        self.set_weather_icon(self.weatherIcon, weather['weather'])

        for n, forecast in enumerate(forecasts['list'][:5], 1):
            getattr(self, 'forecastTime%d' % n).setText(
                from_ts_to_time_of_day(forecast['dt']))
            self.set_weather_icon(
                getattr(self, 'forecastIcon%d' % n), forecast['weather'])
            getattr(self, 'forecastTemp%d' % n).setText(
                "%.1f °C" % forecast['main']['temp'])

    def set_weather_icon(self, label, weather):
        label.setPixmap(
            QPixmap(os.path.join('images', "%s.png" %
                                 weather[0]['icon']
                                 )
                    )

        )
    # end weather


def get_cpu_temp():
    #temp = 46
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
