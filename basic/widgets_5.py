from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QListWidget,
    QMainWindow,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5")

        widget = QListWidget()
        widget.addItems(["ONE", "TWO", "THREE"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print("index:", i.text())

    def text_changed(self, s):
        print("text:", s)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
