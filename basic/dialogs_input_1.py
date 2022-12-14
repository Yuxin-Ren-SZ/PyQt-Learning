from PyQt5.QtWidgets import (
    QApplication,
    QInputDialog,
    QMainWindow,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5")

        button1 = QPushButton("Integer")
        button1.clicked.connect(self.get_Int)

        self.setCentralWidget(button1)

    def get_Int(self):
        int_value, ok = QInputDialog.getInt(
            self, "get an int", "enter a number"
        )
        print("result: ", ok, int_value)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
