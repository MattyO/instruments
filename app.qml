import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1

import "screens"

Window {
    id: root
    height:1280
    width: 800

    ColumnLayout{
      anchors.fill: parent
      Rectangle {
        anchors.fill: parent
        color: "black"
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
