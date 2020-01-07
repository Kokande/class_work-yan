from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.diam = [200 for i in range(8)]
        self.color = [(0, 0, 0) for i in range(8)]
        self.pressed = False
        uic.loadUi("UI.ui", self)
        self.button.clicked.connect(self.newd)

    def newd(self):
        self.pressed = True
        for i in range(8):
            self.diam[i] = randint(20, 200)
            self.color[i] = (randint(0, 256), randint(0, 256), randint(0, 256))

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.pressed:
            self.action(qp)
        qp.end()

    def action(self, qp):
        qp.begin(self)
        for i in range(0, 600, 200):
            for k in range(0, 600, 200):
                if i == k == 200:
                    continue
                ind = i // 200 + (k // 200) * 3 - 2
                qp.setPen(QPen(QColor(self.color[ind][0],
                                      self.color[ind][1],
                                      self.color[ind][2]), 2))
                diam = self.diam[ind]
                margin = (200 - diam) // 2
                qp.drawEllipse(i + margin, k + margin, diam, diam)
        qp.end()
        self.update()


if __name__ == '__main__':
    app = QApplication([])
    ex = MainApp()
    ex.show()
    sys.exit(app.exec())