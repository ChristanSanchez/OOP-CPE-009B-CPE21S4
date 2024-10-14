import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()  # Fixed the super() call
        self.title = "PyQt Button"  # Fixed assignment operator
        self.x = 200  # Fixed assignment operator
        self.y = 200  # Fixed assignment operator
        self.width = 300  # Fixed assignment operator
        self.height = 300  # Fixed spelling and assignment operator
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))  # Fixed filename

        self.button = QPushButton('Click me!', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(110, 80)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Fixed parameter order
    ex = App()
    sys.exit(app.exec_())
