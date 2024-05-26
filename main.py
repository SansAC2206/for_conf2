import telebot
from telebot import types
import datetime

print(datetime.datetime.now())

bot = telebot.TeleBot('')
file_path = 'instructions.txt'

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn = types.KeyboardButton("Действия с инструкциями")

    markup.add(btn)

    bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['all_instructions'])
def all_instructions(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Прочитать все инструкции')
    btn2 = types.KeyboardButton('Оставить ответ на инструкцию')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text='Выберете действие', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def func(message):
    if (message.text == 'Оставить ответ на инструкцию'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Оставить ответ на инструкцию 1')
        btn2 = types.KeyboardButton('Оставить ответ на инструкцию 2')
        markup.add(btn1, btn2)
        bot.send_message(chat_id=message.chat.id, text='Выберете инструкцию для того, чтобы оставить ответ', reply_markup=markup)

    if (message.text == 'Оставить ответ на инструкцию 1'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1)
        bot.send_message(message.chat.id, text='Выберете действие', reply_markup=markup)


    if (message.text == 'Прочитать все инструкции'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Читать инструкцию 1')
        btn2 = types.KeyboardButton('Читать инструкцию 2')
        markup.add(btn1, btn2)
        bot.send_message(chat_id=message.chat.id, text='Выберете инструкцию для чтения', reply_markup=markup)

    if (message.text == 'Читать инструкцию 1'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1)
        bot.send_message(message.chat.id, text='Выберете действие', reply_markup=markup)
        bot.send_document(chat_id=message.chat.id, document=open('instructions.txt', 'rb'))

    if (message.text == 'Читать инструкцию 2'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1)
        bot.send_message(message.chat.id, text='Выберете действие', reply_markup=markup)
        bot.send_document(chat_id=message.chat.id, document=open('instructions2.txt', 'rb'))

    if (message.text == 'Вернуться в меню'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Прочитать все инструкции')
        btn2 = types.KeyboardButton('Изменить инструкции')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text='Выберете действие', reply_markup=markup)



@bot.message_handler(commands=['change_file'])
def change_file(message):
    file_path = open('instructions.txt', 'a')

    with open(file_path, 'a') as file:
        file.write('\n' + message.text)

bot.polling(none_stop=True)
