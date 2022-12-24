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
        title = "Enter an Integer"
        label = "Type your integer here"
        value, ok = QInputDialog.getInt(
            self, title, label, value=0, min=-5, max=5, step=1
        )
        print("Result:", ok, value)

    def get_float(self):
        title = "Enter a float"
        label = "Type your float here"
        my_float_value, ok = QInputDialog.getDouble(
            self,
            title,
            label,
            value=0,
            min=-5.3,
            max=5.7,
            decimals=2,
        )
        print("Result:", ok, my_float_value)

    def get_str_from_list(self):
        title = "select a string"
        label = "/select a fruit from the list"
        items = ["apple", "pear", "orange", "grape"]
        initial_selection = 2
        selected_str, ok = QInputDialog.getItem(
            self,
            title,
            label,
            items,
            current=initial_selection,
            editable=False
        )
        print("Result:", ok, selected_str)

    def get_str(self):
        pass

    def get_text(self):
        pass


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
