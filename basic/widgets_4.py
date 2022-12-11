from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QMainWindow,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5")

        widget = QComboBox()
        widget.addItems(["ONE", "TWO", "THREE"])

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print("index:", i)

    def text_changed(self, s):
        print("text:", s)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
