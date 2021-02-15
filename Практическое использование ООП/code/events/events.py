
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    """ Просто тренировочный класс для описания событий"""
    def __init__(self):

        super().__init__()
        self.initUI() #вызов функции отрисовки, которую мы создадим ниже

    def initUI(self):
        btn = QLabel("press esc to quit", self)
        btn.move(30, 50)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Обработчик событий")

        self.show()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Alt:
            self.close()


if __name__ == '__main__':
    #эта часть сработает только тогда, когда у нас этот файл вызывается не как главный
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


