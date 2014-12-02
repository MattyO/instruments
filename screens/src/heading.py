from pubsub import pub
import PyQt5.Qt as Qt
from PyQt5.Qt import pyqtProperty

class Heading(Qt.QQuickItem):

    heading_changed = Qt.pyqtSignal()
    got_signal = Qt.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Qt.QQuickItem, self).__init__(*args, **kwargs)
        self._heading=0
        pub.subscribe(self.handle_change_position, 'change_position')

    def handle_change_position(self, data={}):
        self.heading = data.get('track', 0)

    @pyqtProperty(float, notify=heading_changed)
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, value):
        self._heading = value
        self.heading_changed.emit()
