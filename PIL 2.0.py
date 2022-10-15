import sys

from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from main import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.im = Image.open(self.fname)
        self.imc = Image.open(self.fname)
        self.degree = 0

        self.pixmap = QPixmap(self.fname)
        self.label.setPixmap(self.pixmap)
        self.pushButton.clicked.connect(self.change_color)
        self.pushButton_2.clicked.connect(self.change_color)
        self.pushButton_3.clicked.connect(self.change_color)
        self.pushButton_4.clicked.connect(self.change_color)
        self.pushButton_5.clicked.connect(self.rotate)
        self.pushButton_6.clicked.connect(self.rotate)

    def change_color(self):
        self.imc = self.im.copy()
        pixels = self.imc.load()
        x, y = self.imc.size
        for i in range(x):
            for j in range(y):
                r, g, b, a = pixels[i, j]
                if self.sender().text() == 'R':
                    pixels[i, j] = r, 0, 0, a
                elif self.sender().text() == 'G':
                    pixels[i, j] = 0, g, 0, a
                elif self.sender().text() == 'B':
                    pixels[i, j] = 0, 0, b, a
                else:
                    pass
        self.imc = self.imc.rotate(self.degree, expand=True)
        self.pixmap = QPixmap.fromImage(ImageQt(self.imc))
        self.label.setPixmap(self.pixmap)

    def rotate(self):
        if self.sender() is self.pushButton_6:
            self.degree -= 90
            degree = -90
        else:
            self.degree += 90
            degree = 90
        self.degree %= 360
        self.imc = self.imc.rotate(degree, expand=True)
        self.pixmap = QPixmap.fromImage(ImageQt(self.imc))
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
