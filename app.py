import os, sys
sys.path.append(os.path.abspath('.'))

import PyQt5.Qt as Qt
from PyQt5.Qt import pyqtProperty
#from bjsonrpc_test import SensorEvent
from pubsub import pub

import events

class Heading(Qt.QQuickItem):

    heading_changed = Qt.pyqtSignal()
    got_signal = Qt.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Qt.QQuickItem, self).__init__(*args, **kwargs)
        self._heading=0
        pub.subscribe(self.handle_change_position, 'change_position')

    def onComponentComplete(self):
        print 'component completed'
        self.got_signal.connect(self.handle_got_signal)

    def handle_change_position(self, data={}):
        self.heading = data.get('track', 0)

    @pyqtProperty(float, notify=heading_changed)
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, value):
        self._heading = value
        self.heading_changed.emit()



app = Qt.QApplication(sys.argv)

Qt.qmlRegisterType(Heading, 'Screens', 1, 0, 'Heading')

engine = Qt.QQmlEngine()
component = Qt.QQmlComponent(engine)
component.loadUrl(Qt.QUrl('app.qml'))
for error in component.errors():
    print error.description()

window = component.create()
window.show()

events.listen()

sys.exit(app.exec_())


