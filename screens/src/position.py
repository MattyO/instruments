# -*- coding: utf-8 -*-
import PyQt5.Qt as Qt
from PyQt5.Qt import pyqtProperty
from PyQt5.QtCore import pyqtSignal

import pubsub


class Position(Qt.QQuickItem):
    lat_changed= Qt.pyqtSignal()
    lng_changed= Qt.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Qt.QQuickItem, self).__init__(*args, **kwargs)
        self._lat= 0
        self._lng= 0
        pubsub.ps.change_position.connect(self.update)

    def update(self, data):
        if 'lat' in data:
            self.lat= data.get('lat', 0)
        if 'lng' in data:
            self.lng= data.get('lng', 0)

    def convert_position(self, lat_or_lng):
        def foo(bar):
            return (bar - int(bar)) * 60

        minutes = foo(lat_or_lng)
        seconds = foo(minutes)
        return "{}° {}'{}''".format(int(lat_or_lng), int(minutes), int(seconds))

    @pyqtProperty(str, notify=lat_changed)
    def lat(self):
        return self.convert_position(self._lat)

    @lat.setter
    def lat(self, value):
        self._lat= value
        self.lat_changed.emit()

    @pyqtProperty(str, notify=lng_changed)
    def lng(self):
        return self.convert_position(self._lng)

    @lng.setter
    def lng(self, value):
        self._lng= value
        self.lng_changed.emit()
