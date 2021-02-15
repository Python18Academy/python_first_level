import sys
from  PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QInputDialog, QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    data = ''

    def initUI(self):
        self.btn = QPushButton(" Добавить дело", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.diary = QLabel("", self)
        self.diary.move(50,50)
        self.diary.setFixedWidth(300)
        self.diary.setFixedHeight(200)

        self.setGeometry(500, 350, 500, 250)
        self.setWindowTitle("работа с инпутом")
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', "введите дело, которое вы хотите исполнить:")
        if ok:
            self.data +=str(text) + "\n"
            self.diary.setText(str(self.data))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
