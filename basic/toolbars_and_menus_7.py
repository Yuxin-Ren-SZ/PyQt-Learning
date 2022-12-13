import os
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QAction,
    QMainWindow,
    QLabel,
    QToolBar,
    QStatusBar,
    QMenuBar,
    QWidget,
    QCheckBox,
)

basdedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5")

        label = QLabel("Hellow")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("Main Toolbar")
        # toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(
            QIcon(os.path.join(basdedir, "image/bug.png")),
            "Button &1",
            self,
        )
        button_action.setStatusTip("this is button")
        button_action.triggered.connect(self.onToolBarClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(
            QIcon(os.path.join(basdedir, "image/bug.png")),
            "Button &2",
            self,
        )
        button_action2.setStatusTip("Button 2")
        button_action2.triggered.connect(self.onToolBarClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

        self.setStatusBar(QStatusBar(self))

    def onToolBarClick(self, s):
        print("click", s)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
