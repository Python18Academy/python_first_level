import os # для работы с файлами нам нужен OS
from tkinter import * # Берем все из tkinter
from tkinter.messagebox import * # для отображения диалоговых окон
from tkinter.filedialog import * # для получения файлов

class Notepad:
    __root = Tk() # вызываем класс Tk, в котором будем собирать окно
    __thisTextArea = Text(__root, font=('Georgia', 30)) # Окно, в котором мы будем писать
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar,tearoff=0) # Создаем menu
    __thisScrollBar = Scrollbar(__thisTextArea) # для прокрутки контента нужен scrollbar
    __file = None

    def __init__(self,**kwargs):

        self.__thisWidth = kwargs['width']
        self.__thisHeight = kwargs['height']
        self.__root.title("Untitled - Notepad")
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, 50, 50))
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)
        self.__thisTextArea.grid(sticky=N+E+S+W)
        self.__thisFileMenu.add_command(label="Новый",command=self.__newFile)
        self.__thisFileMenu.add_command(label="Открыть",command=self.__openFile)
        self.__thisFileMenu.add_command(label="Сохранить",command=self.__saveFile)
        self.__thisFileMenu.add_command(label="Выйти",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="Файл",menu=self.__thisFileMenu)

        self.__root.config(menu=self.__thisMenuBar)
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    
    def __quitApplication(self):
        self.__root.destroy()
        #exit()

    def __openFile(self):
        self.__file = askopenfilename(filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if self.__file == "":
            self.__file = None
        else:
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0,END)
            file = open(self.__file,"r")
            self.__thisTextArea.insert(1.0,file.read())
            file.close()

        
    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):

        if self.__file == None:
            #save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
                
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def run(self):
        self.__root.mainloop()

# запускаем приложение
notepad = Notepad(width=1000,height=700)
notepad.run()



