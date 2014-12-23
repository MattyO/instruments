import QtQuick 2.2
import Screens 1.0
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1

import '../widgets'

Compass{
  height: 80
  implicitWidth: compass_layout.implicitWidth
  RowLayout{
    id: compass_layout
    Repeater {
      model: foo.splice(0, foo.length/2)
      delegate: Item {
        width: 60
        Text{
          anchors.fill: parent
          verticalAlignment: Text.AlignVCenter
          color: "white"
          text: modelData
          font.pointSize: 20 + (index *2)
        }
      }
    }

    Text{
      color: 'white'
      text: heading
      font.pixelSize: 80
    }

    Repeater {
      model: foo.splice((foo.length/2), foo.length)
      delegate: Item{
        width: 60
        Layout.fillHeight: true
        Text{
          anchors.fill: parent
          verticalAlignment: Text.AlignVCenter
          color: "white"
          text: modelData
          font.pointSize: 20 + (foo.length - index *2)
        }
      }
    }
  }
}
