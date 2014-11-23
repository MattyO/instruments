import bjsonrpc
import bjsonrpc.handlers
from pubsub import pub
import threading

class SensorEvents(bjsonrpc.handlers.BaseHandler):
    def change_position(self, position_data):
        print position_data
        pub.sendMessage('change_position', data=position_data)
        return {"message":"got it"}

def listen():
    sensor_events = bjsonrpc.createserver(host="0.0.0.0", port=9001, handler_factory=SensorEvents)
    thread = threading.Thread(target=sensor_events.serve)
    thread.deamon = True
    thread.start()
