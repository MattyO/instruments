import io

import PyQt5.Qt as Qt
#import mpl_toolkits.basemap as basemap
import pubsub

data = {
        'east_end':   (41.7678, -81.2551),
        'lighthouse': (41.7687, -81.2812),
        'west_end':   (41.7687, -81.2781,),
        'geneva':     (41.8582639,-80.9743154),
}


def get_bounds(data_points):
    lats = map(lambda p: p[0], data.values())
    longs = map(lambda p: p[1], data.values())
    return (min(lats), min(longs),max(lats), max(longs))

def get_screen_ratio(height, width):
    return width / height

def map_data(data, pixels_per_unit):
    min_lat,min_lng, max_lat, max_lng = get_bounds(data)
    return { key: (value[0] * pixels_per_unit, value[1]* pixels_per_unit) for key, value in data.items() }

class Map(Qt.QQuickPaintedItem):
    def __init__(self, *args, **kwargs):
        super(Qt.QQuickPaintedItem, self).__init__(*args, **kwargs)
        pubsub.ps.change_position.connect(self.update_stuff)

    def update_stuff(self, updated_data):
        data.update({'me': (updated_data.get('lat', 0), updated_data.get('lng', 0))})
        self.update(self.contentsBoundingRect().toRect())

    #def paint(self, painter):
    #    self.setAntialiasing(True)
    #    pen = Qt.QPen(Qt.QColor('white'), 2)
    #    painter.setPen(pen)
    #    painter.setBrush(Qt.QBrush(Qt.QColor('white')))


    #    min_lat,min_lng, max_lat, max_lng = get_bounds(data)
    #    m = basemap.Basemap(projection='mill',
    #                        resolution='c',llcrnrlat=min_lat,urcrnrlat=max_lat,
    #                                            llcrnrlon=min_lng,urcrnrlon=max_lng)

    #    projected_data = { key:m(value[1], value[0]) for key, value in data.items() }

    #    max_projected_lng = max(map(lambda pos: pos[0], projected_data.values()))
    #    max_projected_lat = max(map(lambda pos: pos[1], projected_data.values()))

    #    screen_ratio = get_screen_ratio(self.height(), self.width())
    #    map_ratio =  get_screen_ratio(max_projected_lat, max_projected_lng)

    #    reduced_screen_height = self.height()
    #    reduced_screen_width = self.width()
    #    x_padding = 100
    #    y_padding = 100

    #    if  map_ratio > screen_ratio:
    #        reduced_screen_width = self.width() - x_padding
    #        reduced_screen_height = reduced_screen_width  * (1/map_ratio)
    #        y_padding = self.height() - reduced_screen_height
    #    else:
    #        reduced_screen_height = self.height() - y_padding
    #        reduced_screen_width = reduced_screen_height * map_ratio
    #        x_padding = self.width() - reduced_screen_width

    #    for place, (lat,lng) in data.items():
    #        projected_lng, projected_lat = m(lng, lat)
    #        x = (projected_lng / max_projected_lng) * reduced_screen_width
    #        y = (projected_lat / max_projected_lat) * reduced_screen_height
    #        x += (x_padding / 2)
    #        y += (y_padding / 2)

    #        if place == 'me':
    #            pen = Qt.QPen(Qt.QColor('blue'), 2)
    #            painter.setPen(pen)
    #            painter.setBrush(Qt.QBrush(Qt.QColor('blue')))
    #        painter.drawEllipse(x-5, self.height() - y - 5, 10, 10)
    #        if place =='me':
    #            pen = Qt.QPen(Qt.QColor('white'), 2)
    #            painter.setPen(pen)
    #            painter.setBrush(Qt.QBrush(Qt.QColor("white")))
    #        #painter.drawPoint(x-5, self.height() - y - 5, 10, 10)
