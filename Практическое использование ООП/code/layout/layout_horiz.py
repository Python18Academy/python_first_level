"""" простое приветствие на Python"""

import sys
#без sys у нас даже приложение не запуститься
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
# sys argv позволяет нам принимать аргументы из командной строки
#если вам этого не нужно, то можете оставить скобки пустыми

window = QWidget()
#создать окно
window.setWindowTitle("Первое приветствие на PyQt")
#задать название нашей выполняемой программы
layout = QHBoxLayout()

layout.addWidget(QPushButton("слева"))
layout.addWidget(QPushButton("по центру"))
layout.addWidget(QPushButton("справа"))
window.setLayout(layout)

#нужно вызвать окно отрисовки
window.show()
# нужно не забыть вызвать цикл
sys.exit(app.exec())
