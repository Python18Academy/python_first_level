
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


import os
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #наследуем аттрибуты от родителя

        layout = QVBoxLayout() #вертикальное расположение
        self.editor = QPlainTextEdit()  # мы могли бы также использовать QTextEdit и установить  self.editor.setAcceptRichText(False)

        #устанавливаем  наш QTextEdit конфигурацию редактора
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont) #используем системный шрифт
        fixedfont.setPointSize(16) #делаем размер шрифта в 14. Можете поменять если что
        self.editor.setFont(fixedfont)  # назначить шрифт

        # self.path  содержит в себе путь только что установленного файла
        # Если нет, тогда мы не открыли файла и не открыли ничего
        self.path = None

        layout.addWidget(self.editor)  #добавляем в наш layout наш редактор

        container = QWidget() #создаем базовый виджет
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.resize(700, 700) #здесь у нас создается размер

        self.status = QStatusBar() #Qstatus class предоставлет горизонтальную часть интерфейса которая сообщает о текущем статуса
        self.setStatusBar(self.status)  #принимаем статус

        file_toolbar = QToolBar("File") #здесь у нас описывает окно с файлом
        file_toolbar.setIconSize(QSize(14, 14)) #здесь у нас создаем метод,который устанавливает
        self.addToolBar(file_toolbar)
        file_menu = self.menuBar().addMenu("&File")

        open_file_action = QAction(QIcon(os.path.join('images', 'blue-folder-open-document.png')), "Открыть файл...", self)
        open_file_action.setStatusTip("Открыть файл")
        open_file_action.triggered.connect(self.file_open)
        file_menu.addAction(open_file_action)
        file_toolbar.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join('images', 'disk.png')), "Сохранить", self)
        save_file_action.setStatusTip("Сохранить текущий файл...")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)

        saveas_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Сохранить как...", self)
        saveas_file_action.setStatusTip("Сохранить файл как ...")
        saveas_file_action.triggered.connect(self.file_saveas)
        file_menu.addAction(saveas_file_action)
        file_toolbar.addAction(saveas_file_action)

        edit_toolbar = QToolBar("Edit")
        edit_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar().addMenu("&Edit")

        undo_action = QAction(QIcon(os.path.join('images', 'arrow-curve-180-left.png')), "Undo", self)
        undo_action.setStatusTip("Undo last change")
        undo_action.triggered.connect(self.editor.undo)
        edit_menu.addAction(undo_action)

        redo_action = QAction(QIcon(os.path.join('images', 'arrow-curve.png')), "Redo", self)
        redo_action.setStatusTip("Redo last change")
        redo_action.triggered.connect(self.editor.redo)
        edit_toolbar.addAction(redo_action)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator() # добавить разделить

        cut_action = QAction(QIcon(os.path.join('images', 'scissors.png')), "Cut", self)
        cut_action.setStatusTip("Вырезать выделенный текст")
        cut_action.triggered.connect(self.editor.cut)
        edit_toolbar.addAction(cut_action)
        edit_menu.addAction(cut_action)

        copy_action = QAction(QIcon(os.path.join('images', 'document-copy.png')), "Copy", self)
        copy_action.setStatusTip("Скопировать выделенный текст")
        copy_action.triggered.connect(self.editor.copy)
        edit_toolbar.addAction(copy_action)
        edit_menu.addAction(copy_action)
        edit_menu.addSeparator()

        wrap_action = QAction(QIcon(os.path.join('images', 'arrow-continue.png')), "Wrap text to window", self)
        wrap_action.setStatusTip("Toggle wrap text to window")
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.triggered.connect(self.edit_toggle_wrap)  #работает со сносом текста
        edit_menu.addAction(wrap_action)

        self.update_title()
        self.show()

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")

        if path:
            try:
                with open(path, 'rU') as f:
                    text = f.read()

            except Exception as e:
                self.dialog_critical(str(e))

            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()

    def file_save(self):
        if self.path is None:
            # Если пути нет, тогда мы открываем окно сохранить как
            return self.file_saveas()

        self._save_to_path(self.path)

    def file_saveas(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);All files (*.*)")

        if not path:
            #Если диалог у нас закончился, тогда вернет целое ничего''
            return

        self._save_to_path(path)

    def _save_to_path(self, path):
        text = self.editor.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.update_title()


    def update_title(self):
        self.setWindowTitle("%s - No2Pads" % (os.path.basename(self.path) if self.path else "Untitled"))

    def edit_toggle_wrap(self):
        self.editor.setLineWrapMode( 1 if self.editor.lineWrapMode() == 0 else 0 )


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("Notepads 2000")
    window = MainWindow()
    app.exec_()