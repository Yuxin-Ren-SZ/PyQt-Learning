import sys

from PyQt5.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

window = QPushButton("Button")
window.show()

app.exec()
