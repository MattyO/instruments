import QtQuick 2.2
import Screens 1.0
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1

import '../widgets'

WindDirection{
  height: 200
  width: 200
  InstReading{
    title: "Wind Direction"
    reading: wind_direction
  }
}
