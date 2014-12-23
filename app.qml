import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1

import "screens"

Window {
  id: root
  height:1280
  width: 800

  Rectangle {
    anchors.fill: parent
    color: "black"
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
        Heading {}

        Speed {}

        Position {}

        WindSpeed {}

        WindDirection {}
      }
    }
  }
}
