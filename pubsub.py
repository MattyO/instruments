import PyQt5.Qt as Qt

class pubsub(Qt.QObject):
    change_position = Qt.pyqtSignal(dict)
    set_mark = Qt.pyqtSignal(float, float)
    change_speed = Qt.pyqtSignal(float)

ps = pubsub()
