import bjsonrpc
import bjsonrpc.handlers
import PyQt5.Qt as Qt

import pubsub


class SensorEvents(bjsonrpc.handlers.BaseHandler):
    def change_position(self, position_data):
        print 'getting data'
        pubsub.ps.change_position.emit(position_data)
  
class QSensorThread(Qt.QThread):
    def run(self):
        sensor_events = bjsonrpc.createserver(host="0.0.0.0", port=9001, handler_factory=SensorEvents)
        sensor_events.serve()

