"""Пример расположения с помощью верстки"""

import sys
#без sys у нас даже приложение не запуститься
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton

app = QApplication(sys.argv)
# sys argv позволяет нам принимать аргументы из командной строки
#если вам этого не нужно, то можете оставить скобки пустыми

window = QWidget()
#создать окно
window.setWindowTitle("Пример верстки формы")
#задать название нашей выполняемой программы
layout = QFormLayout()

layout.addRow("имя",  QLineEdit())
layout.addRow("Возраст",  QLineEdit())
layout.addRow("Работа",  QLineEdit())
layout.addRow("Ваше хобби",  QLineEdit())
layout.addRow(QPushButton("Отправьте все эти данные!"))

window.setLayout(layout)

#нужно вызвать окно отрисовки
window.show()
# нужно не забыть вызвать цикл
sys.exit(app.exec())
