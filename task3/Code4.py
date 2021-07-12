import http.client
import json
from tkinter import *
import tkinter as tk

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "5617f65aa1msh9800793ce9b054cp1fa83bjsna5509d7e4861",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
res = conn.getresponse()
data = res.read()

# К-ть країн які будуть взяті з сайту
a=10

# Створення вікна для відображення всієї інформації
win = tk.Tk()
win.title("Statistics")
win.geometry('600x1080')
win['bg']='#F5A993'

# Функція оновлення всієї інформації та заповнення з сайту новою
def Refresh():
    import json
    TextBox.delete(1.0,END)
    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    all_data = data.decode("utf-8")
    json = json.loads(all_data)


    for i in range(a):
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[14])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[12])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[13])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[10])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[11])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[2])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[3])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', '--------------------')

# Кнопка оновлення
Refreshbutton = Button(text="REFRESH", command=Refresh)
Refreshbutton['bg']='grey'
Refreshbutton['fg']='white'
Refreshbutton.pack(side=TOP)

# Параметри тексту
TextBox = Text(width=600, height=500)
TextBox['bg']='#F5A993'
TextBox['fg']='black'
TextBox.pack(side=BOTTOM)

# Запуск функції оновлення, щоб при першому запуску програми не було пустого екрану
Refresh()

win.mainloop()
