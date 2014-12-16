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
        reading: speed
        units: 'kts'
      }

      InstReading{
        title: "Position"
        reading: lat + "<br/>" + lng
      }

      InstReading{
        title: "Wind Speed"
        reading:  wind_speed
        units: 'kts'
      }
      InstReading{
        title: "Wind Direction"
        reading: wind_direction 
      }
    }
  }
}
