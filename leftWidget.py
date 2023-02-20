from PyQt5.QtWidgets import *

from sample.sampleWidget import SampleWidget
from theme.qt_sass_theme.qtSassTheme import QtSassTheme


class LeftWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initUi()

    def __initUi(self):
        self.__label = QLabel('Sample: ')
        lay = QHBoxLayout()
        lay.addWidget(self.__label)
        lay.setContentsMargins(0, 0, 0, 0)
        navWidget = QWidget()
        navWidget.setLayout(lay)
        lay = QVBoxLayout()
        self.__sampleWidget = SampleWidget()
        lay.addWidget(navWidget)
        lay.addWidget(self.__sampleWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)

    def getSampleWidget(self):
        return self.__sampleWidget


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = LeftWidget()
    g = QtSassTheme()
    g.getThemeFiles(theme='light_blue')
    g.setThemeFiles(main_window=w)
    w.show()
    sys.exit(app.exec())