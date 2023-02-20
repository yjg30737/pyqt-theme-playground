from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from widgets.pyqt.pyqt_drawer import Drawer
from widgets.pyqt.pyqt_instant_search_bar import InstantSearchBar
from widgets.pyqt.pyqt_slideshow import SlideShow
from widgets.qml.slider import Slider


class SampleWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initUi()

    def __initUi(self):
        # tab 1
        checkBox = QCheckBox()
        checkBox.setText('CheckBox')
        lineEdit = QLineEdit()
        lineEdit.setPlaceholderText('Input...')
        comboBox = QComboBox()
        comboBox.addItems([f'Item {i}' for i in range(1, 6)])
        spinBox = QSpinBox()
        spinBox.setRange(1, 100)
        timeEdit = QTimeEdit()

        lay = QVBoxLayout()
        lay.addWidget(checkBox)
        lay.addWidget(lineEdit)
        lay.addWidget(comboBox)
        lay.addWidget(spinBox)
        lay.addWidget(timeEdit)
        lay.setAlignment(Qt.AlignTop)

        tab1LeftWidget = QGroupBox()
        tab1LeftWidget.setTitle('GroupBox')
        tab1LeftWidget.setLayout(lay)

        label = QLabel('TextEdit')
        textEdit = QTextEdit()
        textEdit.setPlaceholderText('Write something...')
        tab1RightWidget = QWidget()

        lay = QVBoxLayout()
        lay.addWidget(label)
        lay.addWidget(textEdit)
        tab1RightWidget.setLayout(lay)

        lay = QHBoxLayout()
        lay.addWidget(tab1LeftWidget)
        lay.addWidget(tab1RightWidget)

        tab1Widget = QSplitter()
        tab1Widget.addWidget(tab1LeftWidget)
        tab1Widget.addWidget(tab1RightWidget)

        # table & list & tree & chart ...
        tableWidget = QTableWidget()
        listWidget = QListWidget()
        treeWidget = QTreeWidget()
        splitter = QSplitter()

        splitter.addWidget(tableWidget)
        splitter.addWidget(listWidget)
        splitter.addWidget(treeWidget)

        lay = QHBoxLayout()
        lay.addWidget(splitter)

        tab2Widget = QWidget()
        tab2Widget.setLayout(lay)

        comingSoonLbl1 = QLabel('Coming Soon')
        comingSoonLbl1.setAlignment(Qt.AlignCenter)
        comingSoonLbl2 = QLabel('Coming Soon')
        comingSoonLbl2.setAlignment(Qt.AlignCenter)

        # FIXME fix the choppy svg quality of customized widget
        # slideShow = SlideShow()
        # slideShow.setFilenames(['a.png', 'b.png'])
        #
        # listWidget = QListWidget()
        # listWidget.addItems(
        #     ['Age of Empires II: Definitive Edition', 'American Truck Simulator', 'Arma 3', "Assassin's Creed"])
        # drawer = Drawer(self, listWidget)

        # instantSearchBar = InstantSearchBar()

        lay = QHBoxLayout()
        lay.addWidget(comingSoonLbl1)
        # lay.addWidget(drawer)
        # lay.addWidget(slideShow)
        # lay.addWidget(instantSearchBar)

        tab3Widget = QWidget()
        tab3Widget.setLayout(lay)

        # slider = Slider()
        # slider.setOrientation(Qt.Vertical)

        lay = QVBoxLayout()
        lay.addWidget(comingSoonLbl2)

        tab4Widget = QWidget()
        tab4Widget.setLayout(lay)

        tabWidget = QTabWidget()
        tabWidget.addTab(tab1Widget, 'Usual Widgets')
        tabWidget.addTab(tab2Widget, 'View Widgets')
        tabWidget.addTab(tab3Widget, 'PyQt Customized Widgets')
        tabWidget.addTab(tab4Widget, 'Qt Quick Controls')

        lay = QGridLayout()
        lay.addWidget(tabWidget)

        self.setLayout(lay)