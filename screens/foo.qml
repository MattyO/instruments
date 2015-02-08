import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2
import QtQuick.Controls 1.2


MarkForm{
  Text{
    color: 'white'
    text: 'foobar'
  }

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
      onClicked: root.foo() //dialog.visible = false
    }
  }
}
