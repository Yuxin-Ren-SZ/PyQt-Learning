from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QToolBar,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5")

        label = QLabel("Hellow")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

    def onToolBarClick(self, s):
        print("click", s)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
