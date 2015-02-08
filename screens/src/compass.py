import PyQt5.Qt as Qt

import pubsub

class Compass(Qt.QQuickItem):

    heading_changed = Qt.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Qt.QQuickItem, self).__init__(*args, **kwargs)
        self._heading=0
        pubsub.ps.change_position.connect(self.update)

    def update(self, data):
        if 'heading' in data:
            self.heading = data.get('heading', 0)

    @Qt.pyqtProperty(float, notify=heading_changed)
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, value):
        self._heading = value
        self.heading_changed.emit()

    @Qt.pyqtProperty('QStringList', notify=heading_changed)
    def foo(self):
        ones = self.heading % 10
        if self.heading % 10 == 0:
            left_ten = self.heading -10
            right_ten = self.heading + 10
        else:
            left_ten = self.heading - ones
            right_ten = self.heading + 10 - ones

        left_set = [ left_ten - (20*i) for i in range(0,5) ]
        left_set.reverse()
        right_set = [ right_ten + (20*i) for i in range(0,5) ]

        return [str((i+360)%360) for i in left_set+right_set]


        #return [str((abs(18/2 - i) * 10) - self.heading) for i in range(0,18)]

