import QtQuick 2.12
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12
import QtQuick.Controls.Universal 2.12
import QtQuick.Layouts 1.14
import Qt.labs.settings 1.0

Rectangle {
    signal moved(v: int)
    height: 40
    visible: true
    layer.enabled: true
    Slider {
        id: slider
        anchors.centerIn: parent
        implicitWidth: parent.width - 30
        from: 1
        value: 25
        to: 100
        onMoved: {
            parent.moved(value)
        }
    }
}