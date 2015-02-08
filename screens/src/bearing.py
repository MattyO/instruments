# -*- coding: utf-8 -*-
import math
import PyQt5.Qt as Qt
from PyQt5.Qt import pyqtProperty
from PyQt5.QtCore import pyqtSignal

import pubsub

class Bearing(Qt.QQuickItem):

    bearing_changed = Qt.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Qt.QQuickItem, self).__init__(*args, **kwargs)
        self._bearing = None
        pubsub.ps.change_position.connect(self.update)
        pubsub.ps.set_mark.connect(self.update_mark)

        self.current_lat = None
        self.current_lng = None
        self.mark_lat    = None
        self.mark_lng    = None

    def calc_bearing(self):
        lat_diff = self.current_lat - self.mark_lat
        lng_diff = self.current_lng - self.mark_lng
        b = int(math.degrees(float(math.atan(math.fabs(lat_diff)) / math.fabs(lng_diff))))
        return str(b)
        if lat_diff >= 0 and lng_diff >= 0:
            return str(b)
        elif lat_diff <= 0 and lng_diff >= 0:
            return str(b + 90)
        elif lat_diff <= 0 and lng_diff <= 0:
            return str(b + 180)
        elif lat_diff >= 0 and lng_diff <=0:
            return str(b + 270)

    def update_mark(self, lat, lng):
        self.mark_lat = float(lat)
        self.mark_lng = float(lng)

        if self.current_lat is not None and self.current_lng is not None:
            self.bearing = self.calc_bearing()

    def update(self, data):
        if 'lat' in data and 'lng' in data:
            self.current_lat = data['lat']
            self.current_lng = data['lng']
            if self.mark_lat is not None and self.mark_lng is not None:
                self.bearing = self.calc_bearing()

    @pyqtProperty(str, notify=bearing_changed)
    def bearing(self):
        return self._bearing

    @bearing.setter
    def bearing(self, value):
        self._bearing = value
        self.bearing_changed.emit()
