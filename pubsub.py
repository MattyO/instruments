import PyQt5.Qt as Qt
class pubsub(Qt.QObject):
    change_position = Qt.pyqtSignal(dict)

ps = pubsub()
