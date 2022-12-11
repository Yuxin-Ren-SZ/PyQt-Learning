# from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QSpinBox,
    QDoubleSpinBox,
    QMainWindow,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5")

        # widget = QSpinBox()
        widget = QDoubleSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # widget.setRange(-10, 3)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3)
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(
            self.value_changed_str
        )

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s):
        print(s)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
