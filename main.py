# -*- coding: utf-8 -*-
import psycopg2
import telebot
from telebot import types
from request_functions import (weather_today, dog_picture_url, my_ip)

token = "6171321408:AAEk9DYD9nfus6kpRz0cpK21b2umByBkGp0"

bot = telebot.TeleBot(token)

conn = psycopg2.connect(database="lab7",
                             user="postgres",
                             password="123",
                             host="localhost",
                             port="5432")
cursor = conn.cursor()

def get_schedule(day):
    cursor.execute(f"SELECT * \
                    FROM timetable t \
                    WHERE t.day = '{day}';")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(row)
    return result

a = get_schedule('Monday')
print(a)

def cm_select(table_name):
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(row[0])
    result_str =', '.join(result)
    return result_str


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add("/timetable", "/help", "/easter_eggs")
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}!\
                    \nХотите узнать свежую информацию о МТУСИ?(Хочу/Не хочу)\
                    \nДля просмотра моих возможностей воспользуйтесь командой /help\
                    \nДля перехода к таблице с расписание воспользуйтесь командой /timetable ', reply_markup=keyboard)


@bot.message_handler(commands=['timetable'])
def timetable(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Even_Week",
                 "Odd_Week", "This_Week_Is", "/easter_eggs")
    bot.send_message(message.chat.id, f'Таблица с расписанием', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Бот с расписанием...')


@bot.message_handler(commands=['easter_eggs'])
def easter_eggs(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add("/Moscow_weather_today", "/Dog_picture", "/My_ip", "/timetable")
    bot.send_message(message.chat.id,
    'Я могу:\
    \nПоказать погоду в Москве(/Moscow_weather_today),\
    \nПоказать собаку(/Dog_picture),\
    \nПоказать ваш ip адресс(/My_ip),\
    \nОткрать расписание(/timetable)', reply_markup=keyboard)



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
    elif message.text == "Monday":
        schedule = get_schedule('Monday')
        formatted_schedule = '\n'.join([f"{row[1]}\n\
{row[2]} {row[3]} {row[4]} {row[5]} {row[6]} " for row in schedule])
        bot.send_message(message.chat.id, formatted_schedule)
    elif message.text == "Tuesday":
        schedule = get_schedule('Tuesday')
        formatted_schedule = '\n'.join([f"{row[1]}\n\
{row[2]} {row[3]} {row[4]} {row[5]} {row[6]} " for row in schedule])
        bot.send_message(message.chat.id, formatted_schedule)
    elif text == "не хочу":
        bot.send_message(message.chat.id, 'Тогда вам не сюда - https://mtuci.ru/')
    elif text == "не знаю":
        bot.send_message(message.chat.id, 'Зато я знаю, вам сюда - https://mtuci.ru/')
    else:
        bot.send_message(message.chat.id, 'Я вас не понял, думаю, что вам сюда - https://mtuci.ru/')


bot.polling(non_stop=True)