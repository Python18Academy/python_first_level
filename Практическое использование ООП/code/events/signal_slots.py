
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
import random


def greeting():
    """ slot функция, которая передает у нас приветствие"""
    if msg.text():
        msg.setText("")
    else:
        msg.setText(str(random.randint(0, 10)))

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Сигналы и слоты, которые у нас передаются в этом приложении")
layout = QVBoxLayout()

btn = QPushButton("Привет")
btn.clicked.connect(greeting)

layout.addWidget(btn)
msg = QLabel('')

layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())







