import QtQuick 2.2
import Screens 1.0
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1

import '../widgets'

Heading {
    height: 200
    width: 200
    InstReading{
      automation_type: 'heading'
      title: "Heading"
      reading: heading
    }
}
