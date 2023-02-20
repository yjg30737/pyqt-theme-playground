from PyQt5.QtCore import QPropertyAnimation, QAbstractAnimation, pyqtSignal, Qt
from PyQt5.QtWidgets import QMenuBar, QToolButton, QPushButton


class HidableMenuBar(QMenuBar):
    hideSignal = pyqtSignal(bool)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hide_flag = False
        self.__initUi()
    
    def __initUi(self):
        self.setMouseTracking(True)

        tool_button = self.findChild(QToolButton)
        tool_button.setArrowType(Qt.RightArrow)

        self.__showToggleBtn = QPushButton(self)
        self.__showToggleBtn.clicked.connect(self.__hideMenu)
        self.__showToggleBtn.setToolTip('Hide the menu bar')
        self.__showToggleBtn.setIcon('ico/close.svg')

        self.setCornerWidget(self.__showToggleBtn)

        height = self.sizeHint().height()

        self.__menuAnimation = QPropertyAnimation(self, b"height")
        self.__menuAnimation.valueChanged.connect(self.setFixedHeight)

        self.__menuAnimation.setStartValue(height)
        self.__menuAnimation.setDuration(200)  # default duration
        self.__menuAnimation.setEndValue(1)  # default end value

    def __showMenu(self):
        self.__menuAnimation.setDirection(QAbstractAnimation.Backward)
        self.__menuAnimation.start()
        self.__hide_flag = False
        self.hideSignal.emit(self.__hide_flag)

    def __hideMenu(self):
        self.__menuAnimation.setDirection(QAbstractAnimation.Forward)
        self.__menuAnimation.start()
        self.__hide_flag = True
        self.hideSignal.emit(self.__hide_flag)

    def enterEvent(self, e):
        if self.__hide_flag:
            self.__showMenu()
        return super().enterEvent(e)

    def event(self, e):
        if int(e.type()) == 76:
            height = self.sizeHint().height()
            self.__menuAnimation.setStartValue(height)
        return super().event(e)