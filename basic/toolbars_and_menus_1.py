from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QAction,
    QMainWindow,
    QLabel,
    QToolBar,
    QStatusBar,
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

        button_action = QAction("Button", self)
        button_action.setStatusTip("this is button")
        button_action.triggered.connect(self.onToolBarClick)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onToolBarClick(self, s):
        print("click", s)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
