import QtQuick 2.2
import QtQuick.Controls 1.2

Item{
  property string title
  property string reading

  width: 400
  height: 200
  id: root
  Text {
    id: heading
    text: title
    font.pointSize: 20
    anchors.top: root.top
    color: 'white'
  }
  Text{
    id: heading_value
    text: reading
    font.pointSize: 80
    color: 'white'
    anchors.bottom: root.bottom
  }
}
