import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Midterm in OOP"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(300, 300, 400, 400)
        self.setWindowIcon(QIcon('Feather.svg'))

        self.label = QLabel('Enter Full Name:', self)
        self.label.setStyleSheet("color: red;")
        self.label.move(50, 150)

        self.textbox = QLineEdit(self)
        self.textbox.move(145, 145)

        self.button = QPushButton('Display Full Name', self)
        self.button.setStyleSheet("color: red;")
        self.button.move(45, 175)
        self.button.clicked.connect(self.on_click)

        self.result_textbox = QLineEdit(self)
        self.result_textbox.move(145, 175)

        self.show()

    @pyqtSlot()
    def on_click(self):
        full_name = self.textbox.text()
        self.result_textbox.setText(full_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
