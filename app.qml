import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1

import "screens"

Window {
    id: root
    width: 800
    height:1280

    ColumnLayout{
      anchors.fill: parent

      Heading {
      }
      Label {
        text: "test text"
      }
    }
}
