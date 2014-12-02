import signal
import os, sys

import PyQt5.Qt as Qt

import screens.src.heading
import events

sys.path.append(os.path.abspath('.'))

app = Qt.QApplication(sys.argv)

Qt.qmlRegisterType(screens.src.heading.Heading, 'Screens', 1, 0, 'Heading')

engine = Qt.QQmlEngine()
component = Qt.QQmlComponent(engine)
component.loadUrl(Qt.QUrl('app.qml'))
for error in component.errors():
    print error.description()

window = component.create()
for error in component.errors():
    print error.description()
window.show()

#events.listen()
sys.exit(app.exec_())


