import PyQt5.Qt as Qt
from PyQt5.Qt import pyqtProperty
from PyQt5.QtCore import pyqtSignal

import pubsub


class WindDirection(Qt.QQuickItem):
    wind_direction_changed = Qt.pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(Qt.QQuickItem, self).__init__(*args, **kwargs)
        self._wind_direction = 0
        pubsub.ps.change_position.connect(self.update)

    def update(self, data):
        if 'wind_direction' in data:
            self.wind_direction = data.get('wind_direction', 0)

    @pyqtProperty(float, notify=wind_direction_changed)
    def wind_direction(self):
        return self._wind_direction

    @wind_direction.setter
    def wind_direction(self, value):
        self._wind_direction = value
        self.wind_direction_changed.emit()
