from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
)

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5")

        widget = Color("red")

        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
