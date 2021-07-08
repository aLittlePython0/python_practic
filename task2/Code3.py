import tkinter as tk
from tkinter import messagebox
import math
# Функція для переводу числа в двійкову систему числення
def TranslateIn2():
    value = calc.get()
    b = ''
    n=int(value)
    while n > 0 :
            b = str(n % 2) + b
            n = n // 2
    calc['state']= tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,b)
# Функція для знаходження логарифма з основою 2
def Log():
    value=calc.get()
    x=float(value)
    value=math.log2(x)
    calc['state']= tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,value)
# Функція для знаходження сінуса
def Sinus():
    value=calc.get()
    x=float(value)
    value=math.sin(x)
    calc['state']= tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,value)
# Функція для знаходження косінуса
def Cosinus():
    value=calc.get()
    x=float(value)
    value=math.cos(x)
    calc['state']= tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,value)
# Функція для знаходження тангенса
def tgs():
    value=calc.get()
    x=float(value)
    value=math.tan(x)
    calc['state']= tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,value)
# Функція для знаходження котангенса
def ctgs():
    value=calc.get()
    x=float(value)
    value=math.cos(x)/math.sin(x)
    calc['state']= tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,value)
# Функція для знаходження логарифма з основою 10
def Ln():
    value=calc.get()
    x=float(value)
    value=math.log10(x)
    calc['state']= tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,value)
# Функція для запису чисел
def add_digit(digit):
	value = calc.get()
	if value[0]=='0' and len(value)==1:
		value = value[1:]
	calc.delete(0, tk.END)
	calc.insert(0, value + digit)
# Функція для запису операцій на екран
def add_operation(operation):
	value = calc.get()
	if value[-1] in '-+/*%':
		value = value[:-1]
	elif '+' in value or '-' in value or '*' in value or '/' in value:
		calculate()
		value = calc.get()
	calc.delete(0, tk.END)
	calc.insert(0, value + operation)
# Функція для підрахунку операцій
def calculate():
	value = calc.get()
	if value[-1] in '+-/*':
		value = value+value[:-1]
	calc.delete(0, tk.END)
	# Перевірка на цифри та на ділення на 0
	try:
		calc.insert(0, eval(value))
	except (NameError, SyntaxError):
		messagebox.showinfo('Увага', 'Потрібні тільки цифри')
		calc.insert(0, 0)
	except ZeroDivisionError:
		messagebox.showinfo('Увага', 'На нуль ділити не можна!')
		calc.insert(0, 0)
# Функції для виклику функцій які були описані вище
def LogButton(op):
    return tk.Button(font=('Arial',15),text=op,command=Log,bd=5,bg='#92949C')

def perevodB2(op):
    return tk.Button(font=('Arial',15),text=op,command=TranslateIn2,bd=5,bg='#92949C')

def SinButton(op):
    return tk.Button(font=('Arial',15),text=op,command=Sinus,bd=5,bg='#92949C')

def CosButton(op):
    return tk.Button(font=('Arial',15),text=op,command=Cosinus,bd=5,bg='#92949C')

def TgButton(op):
    return tk.Button(font=('Arial',15),text=op,command=tgs,bd=5,bg='#92949C')

def CtgButton(op):
    return tk.Button(font=('Arial',15),text=op,command=ctgs,bd=5,bg='#92949C')

def LnButton(op):
    return tk.Button(font=('Arial',15),text=op,command=Ln,bd=5,bg='#92949C')


def clear():
	calc.delete(0, tk.END)
	calc.insert(0, 0)

def make_digit_button(digit):
	return tk.Button(text=digit, bd=5, font=('Arial', 13),
	command=lambda: add_digit(digit))

def make_operation_button(operation):
	return tk.Button(text=operation, bd=5, font=('Arial', 13),
	command=lambda: add_operation(operation))

def make_operation_buttono(operation):
	return tk.Button(text=operation, bd=5, font=('Arial', 13),bg='#92949C',
	command=lambda: add_operation(operation))

def make_calc_button(operation):
	return tk.Button(text=operation, bd=5, font=('Arial', 13),
	command=calculate)
def make_clear_button(operation):
	return tk.Button(text=operation, bd=5, font=('Arial', 13),
	command=clear)
# Функція натискання enter
def press_key(event):
	print(repr(event.char))
	if event.char.isdigit():
		add_digit(event.char)
	elif event.char in '+-*/':
		add_operation(event.char)
	elif event.char == '\r':
		calculate()
# Характеристики вікна
win = tk.Tk()
win.title('Калькулятор')
win.geometry("370x275+300+300")
win['bg'] = '#F5A993'
# Іконка у верхньому лівому кутку вікна
photo = tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)

win.bind('<Key>', press_key)
# Створення поля вводу
calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
# Створення сітки та розтягування їх по ширині
calc.grid(row=0, column=0, columnspan=6, stick='wen', padx=5, pady=3)
# Створення кнопок
make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)
make_operation_buttono('%').grid(row = 1,column = 5,stick='wens',padx=5,pady=5)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)
LogButton('log').grid(row = 3,column = 5,stick='wens',padx=5,pady=5)
perevodB2('bin').grid(row = 4,column = 5,stick='wens',padx=5,pady=5)
SinButton('sin').grid(row = 1,column = 4,stick='wens',padx=5,pady=5)
CosButton('cos').grid(row = 2,column = 4,stick='wens',padx=5,pady=5)
TgButton('tg').grid(row = 3,column = 4,stick='wens',padx=5,pady=5)
CtgButton('ctg').grid(row = 4,column = 4,stick='wens',padx=5,pady=5)
LnButton('ln').grid(row = 2,column = 5,stick='wens',padx=5,pady=5)
# Розміри клавіш
win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
