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
        ps.trigger.connect(self.test_handle)

    def test_handle(self, data):
        print 'in test handle'
        print data
        self.heading = data.get('heading', 0)

    @pyqtProperty(float, notify=heading_changed)
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, value):
        self._heading = value
        self.heading_changed.emit()
