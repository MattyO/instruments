#from pubsub import pub
import PyQt5.Qt as Qt
from PyQt5.Qt import pyqtProperty
from PyQt5.QtCore import pyqtSignal


class pubsub(Qt.QObject):
    trigger = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super(Qt.QObject, self).__init__(*args, **kwargs)


ps = pubsub()

class Heading(Qt.QQuickItem):

    heading_changed = Qt.pyqtSignal()
    speed_changed =Qt.pyqtSignal()
    lat_changed =Qt.pyqtSignal()
    lng_changed = Qt.pyqtSignal()
    wind_speed_changed =Qt.pyqtSignal()
    wind_direction_changed =Qt.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Qt.QQuickItem, self).__init__(*args, **kwargs)
        self._heading=0
        self._speed=0
        self._wind_speed = 0
        self._wind_direction = 0
        self._position = {'lat': "0 0'0''", 'lng': "0 0'0''"}
        ps.trigger.connect(self.test_handle)

    def test_handle(self, data):
        print 'in test handle'
        print data
        self.heading = data.get('heading', 0)
        self.speed = data.get('speed', 0)
        self.lat  = str(data.get("lat", 0))
        self.lng = str(data.get("lng", 0))
        self.wind_speed = data.get("wind_speed", 0)
        self.wind_direction = data.get("wind_direction", 0)

    @pyqtProperty(float, notify=heading_changed)
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, value):
        self._heading = value
        self.heading_changed.emit()

    @pyqtProperty(float, notify=speed_changed)
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value
        self.speed_changed.emit()

    @pyqtProperty(str, notify=lat_changed)
    def lat(self):
        return self._position['lat']

    @lat.setter
    def lat(self, value):
        self._position['lat'] = value
        self.lat_changed.emit()

    @pyqtProperty(str, notify=lng_changed)
    def lng(self):
        return self._position['lng']

    @lng.setter
    def lng(self, value):
        self._position['lng'] = value
        self.lng_changed.emit()

    @pyqtProperty(float, notify=wind_speed_changed)
    def wind_speed(self):
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value):
        print 'setting wind speed to {}'.format(value)
        print type(value)
        self._wind_speed = value
        self.wind_speed_changed.emit()

    @pyqtProperty(int, notify=wind_direction_changed)
    def wind_direction(self):
        return self._wind_direction

    @wind_direction.setter
    def wind_direction(self, value):
        self._wind_direction = value
        self.wind_direction_changed.emit()

