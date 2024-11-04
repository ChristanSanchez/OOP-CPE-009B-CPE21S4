import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "PyQt Button"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height= 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        self.button = QPushButton('Click me!',self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(110,70)
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('You touch my tralala')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())