from PyQt5.QtWidgets import QMainWindow, QPushButton


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(600, 600)
        self.setMaximumSize(600, 600)
        self.setWindowTitle('кружочки')

        self.button = QPushButton(self)
        self.button.setText('Кнопка')
        self.button.resize(200, 200)
        self.button.move(200, 200)