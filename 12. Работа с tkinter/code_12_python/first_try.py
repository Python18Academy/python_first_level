from tkinter import *
root = Tk()
data = ['И что ты тут кликаешь', 'Тебе не с кем поговорить?', 
'здесь могла быть ваша реклама']
i = 0
def change(event):
    global i
    if i == len(data):
        i = 0
    b['text'] = data[i]
    b['activeforeground'] = "red"
    i= i + 1

 
b = Button(text='Кликни для продолжения', width=50, height=15, font = ('Verdana', 30))
b.bind('<Button-1>', change)
b.pack()
 
root.mainloop()
