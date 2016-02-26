# -*- coding: utf-8 -*-
import PyQt5.Qt as Qt
from PyQt5.Qt import pyqtProperty
from PyQt5.QtCore import pyqtSignal

import pubsub

class Heading(Qt.QQuickItem):

    heading_changed = Qt.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Qt.QQuickItem, self).__init__(*args, **kwargs)
        self._heading=0
        self._wind_direction = 0
        pubsub.ps.change_position.connect(self.update)


    def update(self, data):
        if 'track' in data:
            self.heading = round(data.get('track', 0))

    @pyqtProperty(float, notify=heading_changed)
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, value):
        self._heading = value
        self.heading_changed.emit()
