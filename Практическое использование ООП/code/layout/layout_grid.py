"""Пример расположения с помощью верстки"""



import sys
#без sys у нас даже приложение не запуститься
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
# sys argv позволяет нам принимать аргументы из командной строки
#если вам этого не нужно, то можете оставить скобки пустыми

window = QWidget()
#создать окно
window.setWindowTitle("Пример работы сетки на PyQt5")
#задать название нашей выполняемой программы
layout = QGridLayout()

layout.addWidget(QPushButton("кнопка на позиции 0, 0"), 0, 0)
#  В QGridLayout у нас первый аргумент это строка, второй позиция в ней
layout.addWidget(QPushButton("кнопка на позиции 1, 1"), 1, 1)
layout.addWidget(QPushButton("кнопка на позиции 2, 2"), 2, 0)
window.setLayout(layout)

#нужно вызвать окно отрисовки
window.show()
# нужно не забыть вызвать цикл
sys.exit(app.exec())
