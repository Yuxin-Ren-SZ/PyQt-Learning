import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)


def the_button_was_clicked():
    print("Clicked!")


def the_button_was_toggled(checked):
    print("state:", checked)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My PyQt5")

        button = QPushButton("button")
        button.setCheckable(True)
        button.clicked.connect(the_button_was_clicked)
        button.clicked.connect(the_button_was_toggled)

        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
