from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My PyQt5")

        self.button = QPushButton("Button")
        self.button.clicked.connect(self.button_clicked)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        self.button.setText("Clicked")
        self.button.setEnabled(False)

        self.setWindowTitle("Dead PyQt5")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
