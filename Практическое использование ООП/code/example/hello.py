"""" простое приветствие на Python"""

import sys
#без sys у нас даже приложение не запуститься
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
# sys argv позволяет нам принимать аргументы из командной строки
#если вам этого не нужно, то можете оставить скобки пустыми

window = QWidget()
#создать окно
window.setWindowTitle("Первое приветствие на PyQt")
#задать название нашей выполняемой программы
window.setGeometry(400, 400, 800, 800)
#  100 и 100 это параметры по x и y, где у нас должно появиться наше окно
#200, 80 -  это у нас размеры по X и y -  самого окна
# window.move(60, 15)
#двигаемся по x на 60 и по y на 15
helloMSG = QLabel("<h1> Hello  </h1>", parent = window)
helloMSG.move(60, 15)
# window.move(60, 50)
hello2 = QLabel("<h3> ero Ozon </h3>", parent= window)
hello2.move(60, 50)
#нужно вызвать окно отрисовки
window.show()
# нужно не забыть вызвать цикл
sys.exit(app.exec())
