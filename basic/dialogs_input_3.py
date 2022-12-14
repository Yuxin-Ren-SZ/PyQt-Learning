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
        value, isInput = QInputDialog.getInt(
            self, title, label, value=0, min=-5, max=5, step=1
        )
        print("Result:", isInput, value)

    def get_float(self):
        title = "Enter a float"
        label = "Type your float here"
        my_float_value, isInput = QInputDialog.getDouble(
            self,
            title,
            label,
            value=0,
            min=-5.3,
            max=5.7,
            decimals=2,
        )
        print("Result:", isInput, my_float_value)

    def get_str_from_list(self):
        title = "select a string"
        label = "/select a fruit from the list"
        items = ["apple", "pear", "orange", "grape"]
        initial_selection = 2
        selected_str, isInput = QInputDialog.getItem(
            self,
            title,
            label,
            items,
            current=initial_selection,
            editable=False
        )
        print("Result:", isInput, selected_str)

    def get_str(self):
        title = "Enter a string"
        label = "Type your password"
        text = "mypassword"
        mode = QLineEdit.Password
        value, isInput = QInputDialog.getText(
            self,
            title,
            label,
            mode,
            text
        )
        print("Result:", isInput, value)

    def get_text(self):
        title = "Enter text"
        label = "Type your note here"
        value, isInput = QInputDialog.getMultiLineText(
            self,
            title,
            label
        )
        print("Result:", isInput, value)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
