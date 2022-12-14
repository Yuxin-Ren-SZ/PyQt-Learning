from PyQt5.QtWidgets import (
    QApplication,
    QInputDialog,
    QMainWindow,
    QWidget,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5")

        layout = QVBoxLayout()

        button1 = QPushButton("Integer")
        button1.clicked.connect(self.get_int)
        layout.addWidget(button1)

        button2 = QPushButton("Float")
        button2.clicked.connect(self.get_float)
        layout.addWidget(button2)

        button3 = QPushButton("Select")
        button3.clicked.connect(self.get_str_from_list)
        layout.addWidget(button3)

        button4 = QPushButton("String")
        button4.clicked.connect(self.get_str)
        layout.addWidget(button4)

        button5 = QPushButton("Text")
        button5.clicked.connect(self.get_text)
        layout.addWidget(button5)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def get_int(self):
        int_value, ok = QInputDialog.getInt(
            self, "get an int", "enter a number"
        )
        print("result: ", ok, int_value)

    def get_float(self):
        pass

    def get_str_from_list(self):
        pass

    def get_str(self):
        pass

    def get_text(self):
        pass


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
