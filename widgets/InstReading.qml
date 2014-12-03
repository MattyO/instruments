import QtQuick 2.2
import QtQuick.Controls 1.2

Item{
  property string title
  property string reading
  property string units

  width: 400
  height: 200
  id: root
  Text {
    text: title
    font.pointSize: 20
    anchors.bottom: heading_value.top
    anchors.horizontalCenter: root.horizontalCenter
    color: 'white'
  }
  Text{
    id: heading_value
    text: reading
    font.pointSize: reading.indexOf('<br/>') > -1 ? 40 : 80
    color: 'white'
    anchors.verticalCenter: root.verticalCenter
    anchors.horizontalCenter: root.horizontalCenter
  }
  Text{
    anchors.horizontalCenter: root.horizontalCenter
    anchors.top: heading_value.bottom
    text: units
    color: 'white'
    font.pointSize: 20
  }
}
