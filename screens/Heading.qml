import QtQuick 2.2
import Screens 1.0
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1

import '../widgets'

Heading {
  anchors.fill: parent
  Rectangle {
    anchors.fill: parent
    color: "black"
    GridLayout{
      columns: 2
      anchors.fill: parent

      InstReading{
        title: "Heading"
        reading: "100"
      }

      InstReading{
        title: "Speed"
        reading: "5.34"
      }

      InstReading{
        title: "Position"
        reading: "?"
      }

      InstReading{
        title: "Wind Speed"
        reading: "23"
      }
      InstReading{
        title: "Wind Direction"
        reading: "345"
      }
    }
  }
}
