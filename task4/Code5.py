import http.client
import json
import telebot
from telebot import types

# Токін бота
bot = telebot.TeleBot('1866429072:AAG77xLEZcmA1D_O9c4os2Wr1kIaLOd7Vfw')

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "5617f65aa1msh9800793ce9b054cp1fa83bjsna5509d7e4861",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

# Робота бота при його старті, тобто при виконанні команди /start
@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	# Створення та додання кнопки
	btn = types.KeyboardButton("Открыть статистику")
	markup.add(btn)
	# Повідомлення бота при старті
	bot.send_message(message.chat.id, "Привет!\nЯ - {1.first_name}, твой личный бот".format(message.from_user, bot.get_me()),
	parse_mode='html', reply_markup=markup)

# Реакція бота на повідомлення
@bot.message_handler(content_types=['text'])
def text(message):
	if message.chat.type == 'private':
		if message.text == 'Открыть статистику':
			stat(message)
		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
# Функція створення файлу та додання в нього статистики
def stat(message):
	import http.client
	import json
	conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
	res = conn.getresponse()
	data = res.read()
	all_data = data.decode("utf-8")
	json = json.loads(all_data)

	doc = open('Statistics.txt','w')
	doc.write('--------------------\n')

	for i in range(10):
	        doc.write('Continent: ')
	        doc.write(str(json[i].get('Continent')) + '\n')
	        doc.write('Country: ')
	        doc.write(str(json[i].get('Country')) + '\n')
	        doc.write('New Cases: ')
	        doc.write(str(json[i].get('NewCases')) + '\n')
	        doc.write('Total Cases: ')
	        doc.write(str(json[i].get('TotalCases')) + '\n')
	        doc.write('New Deaths: ')
	        doc.write(str(json[i].get('NewDeaths')) + '\n')
	        doc.write('Total Deaths: ')
	        doc.write(str(json[i].get('TotalDeaths')) + '\n')
	        doc.write('Total Recovered: ')
	        doc.write(str(json[i].get('TotalRecovered')) + '\n')
	        doc.write('--------------------\n')
	doc.close()
	# Відкриття файлу
	doc = open('Statistics.txt', 'rb')
	# Бот відправляє файл користувачу
	bot.send_document(message.chat.id, doc)

# Run
bot.polling(none_stop=True)
