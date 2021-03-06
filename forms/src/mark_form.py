import PyQt5.Qt as Qt

import pubsub

class MarkForm(Qt.QQuickItem):

    submited = Qt.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Qt.QQuickItem, self).__init__(*args, **kwargs)

    @Qt.pyqtSlot(float, float)
    def submit(self, lat, lng):
        pubsub.ps.set_mark.emit(lat, lng)
        self.submited.emit()



