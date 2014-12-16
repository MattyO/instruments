import signal
import os, sys
import time

import PyQt5.Qt as Qt

import screens.src.heading
import events
import pqaut.server

import events

sys.path.append(os.path.abspath('.'))
app = None
window=None

def run():
    global app
    global window

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
    #pqaut.server.start_automation_server()

    t = events.QSensorThread()
    t.start()
    sys.exit(app.exec_())


def exit():
    app.exec_()

if __name__ == "__main__":
    run()
