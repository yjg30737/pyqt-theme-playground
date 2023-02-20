from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QMainWindow, QWidget, QSplitter, QMenuBar, QToolBar, QStatusBar, QApplication, QGridLayout
from PyQt5.QtCore import Qt

from leftWidget import LeftWidget
from rightWidget import RightWidget

QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # HighDPI support
QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

# fade menu and tooltip
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setEffectEnabled(Qt.UI_FadeMenu, True)
QApplication.setEffectEnabled(Qt.UI_FadeTooltip, True)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('PyQt Playground')

        menuBar = QMenuBar()
        toolBar = QToolBar()
        statusBar = QStatusBar()

        leftWidget = LeftWidget()
        sampleWidget = leftWidget.getSampleWidget()

        rightWidget = RightWidget()
        rightWidget.setWidgetToControl(sampleWidget)

        mainSplitter = QSplitter()
        mainSplitter.addWidget(leftWidget)
        mainSplitter.addWidget(rightWidget)

        lay = QGridLayout()
        lay.addWidget(mainSplitter)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)

        self.setMenuBar(menuBar)
        self.addToolBar(toolBar)
        self.setStatusBar(statusBar)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())