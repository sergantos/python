from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu


def clicker():
    '''
    Обработка нажатия кнопки Button
    '''
    res = "Привет {}".format(txt.get()) 
    lbl.configure(text=res)

def clicked():
    '''
    Обработка выбора второй RadioButton
    '''
    lbl.configure(text=selected.get()) 

# Создаем окно
window = Tk()
window.title("Тест по огневой подготовке")
window.geometry('1200x600')     # Размер окна

# добавим панель меню
mymenu = Menu(window)
item1 = Menu(mymenu, tearoff=0)    # Создаем список выпадающий из меню "Файл" с отключением начальной пунктирной линии
item1.add_command(label='Создать', command=clicker)
item1.add_command(label='Открыть')
item1.add_command(label='Сохранить')
item1.add_separator()   # добавим разделитель
item1.add_command(label='Закрыть', command=exit)
item2 = Menu(mymenu)    # Создаем список выпадающий из меню "Правка" с начальной пунктирной линией
item2.add_command(label='Отменить')
item2.add_command(label='Повторить')
item2.add_command(label='Выделить')
mymenu.add_cascade(label='Файл', menu=item1)    # Создаем пункт меню "Файл" с выпадающим списком
mymenu.add_cascade(label='Правка', menu=item2)  # Создаем пункт меню "Правка" с выпадающим списком
mymenu.add_command(label='Об авторе')   #   Создаем пунккт меню "Об авторе" без всякого выпадающего списка
window.config(menu=mymenu)

# Добавим вкладки
myTabs = ttk.Notebook(window)   # Создаем группу вкладок
tab1 = ttk.Frame(myTabs)    # Создаем 1-ю вкладку
tab2 = ttk.Frame(myTabs)    # Создаем 2-ю вкладку
myTabs.add(tab1, text="Первая вкладка") # Добавляем в нашу группу вкладок 1-ю вкладку
myTabs.add(tab2, text="Вторая вкладка") # Добавляем в нашу группу вкладок 2-ю вкладку
lbl1 = Label(tab1, text='Это первая вкладка')   # Создаем надпись внутри 1-й вкладки
lbl3 = Label(tab1, text='Строка №2')    # Создаем надпись внутри 1-й вкладки
lbl1.grid(padx=50, pady=50)
lbl3.grid(ipadx=5, ipady=5)
lbl2 = Label(tab2, text='Это вторая вкладка')   # Создаем надпись внутри 2-й вкладки
lbl2.grid(padx=10,pady=10)
myTabs.pack(expand=1, fill='both')  # Объединяем вкладки

window.mainloop()   # Отображаем все на экране
exit()

# Добавляем надпись Label на форму
lbl = Label(window, text="Вопросы по огневой подготовке", font=("Arial Bold", 25))
lbl.grid(column=2, row=0)

# Добавляем текстовое поле на форму
txt = Entry(window, width=10, state="normal")
txt.grid(column=2, row=1)
txt.focus()     # Курсор на этот элемент

# Добавляем внизспадающий список с кучей значений
combo = Combobox(window)
combo['values'] = ("Первый", "Второй", "Третий", 4, 5, "Последний")
combo.current(1)    # установили элемент по-умолчанию "Второй"
combo.grid(column=2, row=2)
print(combo.get())     # Печатаем выбранный элемент т.е. "Второй"

# Добавляем кнопку с обработкой нажатия 
btn= Button(window, text="Ответ", bg="white", fg="black", command=clicker)
btn.grid(column=2, row=3)

# Добавляем чекбокс (квадратный)
chk = Checkbutton(window, text='Выбрать')
chk_state = BooleanVar()  
chk_state.set(True)  # Устанавливаем состояние чекбокса "включен"
chk = Checkbutton(window, text='Выбрать', var=chk_state)  
chk.grid(column=2, row=4) 

# Добавляем Radio-button
selected=IntVar()
rad1 = Radiobutton(window, text="Первая кнопка", value = 1, state="active", variable=selected)
rad2 = Radiobutton(window, text='Вторая кнопка', value = 2, command=clicked, state="active", variable=selected)  
rad3 = Radiobutton(window, text='Третья кнопка', value = 3, variable=selected)
rad1.grid(column=2, row=5)  
rad2.grid(column=2, row=6)  
rad3.grid(column=2, row=7)

# Добавляем текстовую область ScrolledText
txt2 = scrolledtext.ScrolledText(window,width=40,height=10)
txt2.insert(INSERT, "Введите хоть что-нибудь")
txt2.grid(column=2, row=8) 
txt2.delete(1.0, END)   # Передаем координаты очистки

# Создаем всплывающие сообщения
messagebox.showinfo('Мой заголовок', 'Мой текст сообщения')
messagebox.showwarning('Мой заголовок предупреждения', 'Мой текст предупреждения')
messagebox.showerror('Мой заголовок ошибки', 'Мой текст ошибки')

# Создаем опросные окна
myAnswer = messagebox.askquestion("Заголовок вопроса", "Сам вопрос")    # yes no
myAnswer = messagebox.askyesno("Заголовок вопроса", "Сам вопрос")   #   True    False
myAnswer = messagebox.askyesnocancel("Заголовок вопроса", "Сам вопрос") # True  False   None
myAnswer = messagebox.askokcancel("Заголовок вопроса", "Сам вопрос")    # True  False
myAnswer = messagebox.askretrycancel("Заголовок вопроса", "Сам вопрос")     # True  False

# Создаем SpinBox
var = IntVar()
var.set(36)     # Установим значение по-умолчанию в 36
spin = Spinbox(window, from_=0, to=100, width=15, textvariable=var)   # SpinBox от 0 до 100
spin.grid(column=2, row=9)
spin2 = Spinbox(window, values=(3, 8, 11), width=15)   # SpinBox с тремя числами 3, 8, 11
spin2.grid(column=2, row=10)

# Добавляем ProgressBar
# Зададим его стиль и цвет
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green')
# # Создаем прогресс-бар
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 70   # По-умолчанию на 70%
bar.grid(column=2, row=11) 

# Добавляем поле загрузки файла 
# from tkinter import filedialog
file = filedialog.askopenfilename() # выбор одиного файла
# Укажем начальную директорию диалогового окна
from os import path
file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
print(file) #   C:/Users/lavrov-sv/Documents/Default.rdp
files = filedialog.askopenfilenames()   # выбор сразу неколько файлов 
print(files)    #   ('C:/Users/lavrov-sv/Documents/Default.rdp', 'C:/Users/lavrov-sv/Documents/Шахматы.docx')
fileWithExt = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))  # файл по маске
print(fileWithExt)  #   D:/2/jurnal.txt
dir = filedialog.askdirectory() # Запрос выбора каталога
print(dir)  #   D:/2

window.mainloop()   # Отображаем все на экране
exit()