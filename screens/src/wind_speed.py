import PyQt5.Qt as Qt
from PyQt5.Qt import pyqtProperty
from PyQt5.QtCore import pyqtSignal

import pubsub


class WindSpeed(Qt.QQuickItem):
    wind_speed_changed = Qt.pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(Qt.QQuickItem, self).__init__(*args, **kwargs)
        self._wind_speed = 0
        pubsub.ps.change_position.connect(self.update)

    def update(self, data):
        if 'wind_speed' in data:
            self.wind_speed = data.get('wind_speed', 0)

    @pyqtProperty(float, notify=wind_speed_changed)
    def wind_speed(self):
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value):
        self._wind_speed = value
        self.wind_speed_changed.emit()
