import os
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
)

baseDir = os.path.dirname(__file__)
print("PWD: ", os.getcwd())
print("Paths are relative to:", baseDir)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5")

        widget = QLabel("Hello")
        widget.setPixmap(QPixmap(os.path.join(baseDir, "image/otje.jpg")))
        widget.setScaledContents(True)

        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
