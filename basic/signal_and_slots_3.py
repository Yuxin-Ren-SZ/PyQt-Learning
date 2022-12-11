from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)

import sys
from random import choice

window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.times_clicked = 0

        self.setWindowTitle("PyQt 5")

        self.button = QPushButton("Button")
        self.button.clicked.connect(self.button_clicked)

        self.windowTitleChanged.connect(
            self.window_title_changed
        )

        self.setCentralWidget(self.button)

    def button_clicked(self):
        print("Clicked")
        new_title = choice(window_titles)
        print("New title: %s" % new_title)
        self.setWindowTitle(new_title)

    def window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == "Something went wrong":
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
