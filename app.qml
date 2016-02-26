import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2

import "screens"
import "forms"

Window {
  id: root
  height:1280
  width: 800

  Rectangle {
    anchors.fill: parent
    color: "black"
  }

  Button{
    text: "goto"
    height:  50
    width: 50
    z: 1
    anchors.top: parent.top
    anchors.right: parent.right

    style: ButtonStyle {
      background: Rectangle {
        color: 'black'
        border.color: 'white'
      }
      label: Text{
        color: 'white'
        text: control.text
        anchors.fill: parent
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
      }
    }
    onClicked: dialog.visible = true
  }

  Item {
    id: dialog
    visible: false
    z: 1
    anchors.fill: parent
    Rectangle {
      color: 'black'
      anchors.fill: parent
    }

    Rectangle {
      id: background
      color: 'black'
      anchors.horizontalCenter: dialog.horizontalCenter
      anchors.verticalCenter: dialog.verticalCenter
      border.width: 1
      border.color: 'white'
      width: .8 * root.width
      height: .8 * root.height

      MarkForm { }
    }

  }

  ColumnLayout{
    anchors.fill: parent
    Compass {
      Layout.alignment: Qt.AlignCenter
    }

    Item{
      Layout.fillWidth: true
      Layout.fillHeight: true
      GridLayout{
      columns: 2
      anchors.fill: parent
        Speed {}

        Position {}

        Bearing {}

        Heading {}

      }
    }

  }
}
