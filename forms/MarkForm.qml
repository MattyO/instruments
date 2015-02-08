import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2
import QtQuick.Controls 1.2
import Screens 1.0


MarkForm{
  id: root

  onSubmited: root.parent.parent.visible = false

  ColumnLayout{
    Layout.fillWidth: true
    Layout.fillHeight: true

    Text {
      color: "white"
      text: "GO To Position"
    }

    RowLayout{
      Layout.fillWidth: true

      Text {
        height: 50
        width: 200
        text: "Latitude"
        color: 'white'
      }

      TextField {
        property string automation_id: 'lat_text'
        id: lat_text
        height: 50
        width: 200
      }

    }
    RowLayout {
      Layout.fillWidth: true
      Text {
        height: 50
        width: 200
        text: "Longitude"
        color: 'white'
      }

      TextField {
        property string automation_id: 'lng_text'
        id: lng_text
        height: 50
        width: 200
      }
    }
    Button {
      text: "Submit"
      style: ButtonStyle {
        background: Rectangle {
          color: 'green'
        }
      }
      onClicked: root.submit(lat_text.text, lng_text.text)
    }
    Button {
      text: "Cancel"
      style: ButtonStyle {
        background: Rectangle {
          color: "red"
        }
      }
      onClicked: dialog.visible = false
    }
  }
}
