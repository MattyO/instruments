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
        automation_type: 'heading'
        title: "Heading"
        reading: heading
      }

      InstReading{
        title: "Speed"
        reading: "5.34"
        units: 'kts'
      }

      InstReading{
        title: "Position"
        reading: "42°23'51'' W <br/> 82°42'22'' E"
      }

      InstReading{
        title: "Wind Speed"
        reading: "23"
        units: 'kts'
      }
      InstReading{
        title: "Wind Direction"
        reading: "345°"
      }
    }
  }
}
