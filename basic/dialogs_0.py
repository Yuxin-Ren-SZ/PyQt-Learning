from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5")

        button = QPushButton("Press For Dialog")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("clicked", s)

        dlg = QDialog(self)
        dlg.setWindowTitle("diaL")
        dlg.exec()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
