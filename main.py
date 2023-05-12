# -*- coding: utf-8 -*-
import telebot
from telebot import types
from request_functions import weather_today
from request_functions import dog_picture_url
from request_functions import my_ip

token = ""

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    keyboard.row("/help")
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}!\
     Хотите узнать свежую информацию о МТУСИ?(Хочу/Не хочу)', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    keyboard.row("/Moscow_weather_today", "/Dog_picture", "/My_ip")
    bot.send_message(message.chat.id, 'Я умею показывать погоду в Москве(/Moscow_weather_today),\
                                        показать рандомное изображение собаки(/Dog_picture),\
                                        показать ваш ip адресс(/My_ip)', reply_markup=keyboard)

@bot.message_handler(commands=['Moscow_weather_today'])
def start_message(message):
    bot.send_message(message.chat.id, weather_today())

@bot.message_handler(commands=['Dog_picture'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вот фото собаки')
    bot.send_photo(message.chat.id, dog_picture_url())

@bot.message_handler(commands=['My_ip'])
def start_message(message):
    bot.send_message(message.chat.id, f'Ваш ip: {my_ip()}')


@bot.message_handler(content_types=['text'])
def answer(message):
    text = message.text.lower()
    if text == "хочу":
        bot.send_message(message.chat.id, 'Тогда вам сюда - https://mtuci.ru/')
    elif text == "не хочу":
        bot.send_message(message.chat.id, 'Тогда вам не сюда - https://mtuci.ru/')
    elif text == "не знаю":
        bot.send_message(message.chat.id, 'Зато я знаю, вам сюда - https://mtuci.ru/')
    else:
        bot.send_message(message.chat.id, 'Я вас не понял, думаю, что вам сюда - https://mtuci.ru/')


bot.polling(non_stop=True)

