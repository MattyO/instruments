import PyQt5.Qt as Qt
from PyQt5.Qt import pyqtProperty
from PyQt5.QtCore import pyqtSignal

import pubsub


class Speed(Qt.QQuickItem):
    speed_changed = Qt.pyqtSignal()
    def __init__(self, *args, **kwargs):
        super(Qt.QQuickItem, self).__init__(*args, **kwargs)
        self._speed = 0
        pubsub.ps.change_position.connect(self.update)

    def update(self, data):
        if 'speed' in data:
            self.speed = data.get('speed', 0)


    @pyqtProperty(float, notify=speed_changed)
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value
        self.speed_changed.emit()
