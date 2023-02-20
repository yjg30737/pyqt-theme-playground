import os
import sys

from PyQt5.QtCore import Qt, QUrl, QSettings, pyqtSignal
from PyQt5.QtQuickWidgets import QQuickWidget
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QVBoxLayout

# TODO
# https://doc.qt.io/qt-6/qtquickcontrols2-customize.html
# https://wiki.qt.io/Qml_Styling


class Slider(QQuickWidget):
    sliderMoved = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()

    def __initUi(self):
        file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "slider.qml")

        self.setSource(QUrl.fromLocalFile(file))
        self.setMaximumHeight(self.height())
        self.setResizeMode(QQuickWidget.SizeRootObjectToView)

        objForEventHandle = self.rootObject()
        objForEventHandle.moved.connect(self.sliderMoved)

        # objForEventHandle.setProperty('Material.theme', 'Material.Dark')

default_style = "Material"
default_theme = "Dark"

settings = QSettings()
style = settings.value("style")
theme = settings.value("theme")
if not style:
    style = default_style
    settings.setValue("style", style)
if not theme:
    theme = default_theme
    settings.setValue("theme", theme)

os.environ["QT_QUICK_CONTROLS_STYLE"] = style
os.environ["QT_QUICK_CONTROLS_MATERIAL_THEME"] = theme