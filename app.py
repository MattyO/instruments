import signal
import os, sys
import time

import PyQt5.Qt as Qt

import screens.src.heading
import screens.src.speed
import screens.src.position
import screens.src.wind_direction
import screens.src.wind_speed
import screens.src.compass
import screens.src.map
import screens.src.bearing
import forms.src.mark_form
import events
#import pqaut.server

import events

sys.path.append(os.path.abspath('.'))
app = None
window=None

def run():
    global app
    global window

    app = Qt.QApplication(sys.argv)

    Qt.qmlRegisterType(screens.src.heading.Heading,              'Screens', 1, 0, 'Heading')
    Qt.qmlRegisterType(screens.src.speed.Speed,                  'Screens', 1, 0, 'Speed')
    Qt.qmlRegisterType(screens.src.position.Position,            'Screens', 1, 0, 'Position')
    Qt.qmlRegisterType(screens.src.wind_speed.WindSpeed,         'Screens', 1, 0, 'WindSpeed')
    Qt.qmlRegisterType(screens.src.wind_direction.WindDirection, 'Screens', 1, 0, 'WindDirection')
    Qt.qmlRegisterType(screens.src.compass.Compass,              'Screens', 1, 0, 'Compass')
    Qt.qmlRegisterType(screens.src.map.Map,                      'Screens', 1, 0, 'Map')
    Qt.qmlRegisterType(screens.src.bearing.Bearing,              'Screens', 1, 0, 'Bearing')
    Qt.qmlRegisterType(forms.src.mark_form.MarkForm,             'Screens', 1, 0, 'MarkForm')

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
