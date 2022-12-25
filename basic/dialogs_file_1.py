from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt")

        button1 = QPushButton("Open file")
        button1.clicked.connect(self.get_filename)

        self.setCentralWidget(button1)

    def get_filename(self):
        filename, selected_filter = QFileDialog.getOpenFileNames(self)
        print("Result:", filename, selected_filter)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
