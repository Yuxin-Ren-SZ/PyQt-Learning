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
        self.addToolBar(toolbar)

        button_action = QAction(
            QIcon(os.path.join(basdedir, "image/bug.png")),
            "Button",
            self,
        )
        button_action.setStatusTip("this is button")
        button_action.triggered.connect(self.onToolBarClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onToolBarClick(self, s):
        print("click", s)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
