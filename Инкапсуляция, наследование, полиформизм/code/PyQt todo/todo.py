import sys
#импортируем наш sys
import json
#берем json для того, чтобы мы могли сохранять наши дела
from PyQt5 import QtCore, QtGui, QtWidgets, uic
# uic нам нужен для того, чтобы мы могли брать файл дизайна, который мы взяли PyQtDesigner
from PyQt5.QtCore import Qt  #берем ядро нам тот случай, если нам понадобится работа с файлами ( а она нам понадобится)


qt_creator_file = "mainwindow.ui" #здесь лежит наша верстка
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)  #загружаем uis
tick = QtGui.QImage('tick.png') # получаем нашу иконку выполненого дела


class TodoModel(QtCore.QAbstractListModel):
    """
    QAbstractModel дает стандартный интферфейс для модели, которая предоставляет данные в виде
    ниерархического списка айтемов. Обычно не используется напрямую, и наш класс
    наследует его
    """
    def __init__(self, *args, todos=None, **kwargs):
        """ Наш конструктор, у которого по умолчанию у нас нет
        никаких
        """
        super(TodoModel, self).__init__(*args, **kwargs)
        #вызывем атрибуты родителя
        self.todos = todos or []  #создаем список наших дел todos или просто пустой список если ничего нет
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            """Просто отображаем наши дела и их контент"""
            _, text = self.todos[index.row()]
            # получаем только текст
            return text
        
        if role == Qt.DecorationRole:
            #получаем только статус
            status, _ = self.todos[index.row()]
            if status:
                #если у нас есть знак выполнено, тогда мы показываем
                return tick

    def rowCount(self, index):
        """Метод возвращает количество дел, которые у нас есть"""
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """ У нас  здесь происходит множественное наследование
        Мы наследуем от главного окна
        и от класса, в котором у нас наша верстка
    """
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.model = TodoModel() #создаем экземпляр наших дел
        self.load() #загружаем наши дела, которые были сохранены
        self.todoView.setModel(self.model) #устанавливаем нашу модель
        self.addButton.pressed.connect(self.add) #связываем кнопку добавить с событием add
        self.deleteButton.pressed.connect(self.delete) #связываем с удалением
        self.completeButton.pressed.connect(self.complete) #связываем с комплектацией

    def add(self):
        """
        Добавляем item в  наш QLineEdit .todoEdit
        и потом очищаем его после сохранения
        """
        text = self.todoEdit.text()
        if text: # не добавляем пустые строки
            # получаем наши дела из модели
            self.model.todos.append((False, text))
            # запускаем перерисовку
            self.model.layoutChanged.emit()
            # очищаем наш input
            self.todoEdit.setText("")
            self.save()
        
    def delete(self):
        """ Функция удаления дел"""
        indexes = self.todoView.selectedIndexes() #получение индексов нашего дела
        if indexes:
            # если у нас был выделено какое-то дело
            index = indexes[0]
            # Удаляем дело и периросовыем
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # удаляем наше дело
            self.todoView.clearSelection()
            self.save()
            
    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            #если у нас есть хоть какие-то дела
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text) #назначаем нашему делу значение true
            # .dataChanged takes top-left and bottom right, which are equal 
            # для одиночного выделия
            self.model.dataChanged.emit(index, index)
            # очищание выделение
            self.todoView.clearSelection()
            self.save()
    
    def load(self):
        try:
            with open('data.db', 'r') as f:
                #работаем с форматом data.db
                #в них например могут содержаться данные в мобильные приложения
                self.model.todos = json.load(f) # загружаем данные в нашу модель
        except Exception:
            pass #просто промолчим
            #но вообще можно сюда добавить и какое-то логирование

    def save(self):
        #сохраняем нашего дело в виде json
        with open('data.db', 'w') as f:
            data = json.dump(self.model.todos, f)


app = QtWidgets.QApplication(sys.argv)
# создаем экземпляр нашего приложения
window = MainWindow() #создаем экземпляр нашего окна
window.show()  #показать наше окно
app.exec_() # вызывается основной цикл приложения


