import time
import telebot
from telebot import types
from db import db_table_val, db_comment_save
from options import *
from logic import *



bot = telebot.TeleBot(CODE)


@bot.message_handler(commands=['start'])
def start(message):
    us = message.from_user.id
    name = message.from_user.first_name
    fam = message.from_user.last_name
    nik = message.from_user.username
    db_table_val(us, name, fam, nik)
    text1 = f'''<b>{message.from_user.first_name}</b>, прежде чем пройти тест, давайте познакомимся!

Сейчас я расскажу, <b>как связаны самооценка человека и его отношения, карьера и уровень дохода.</b> '''
    video = open('video/video1.mp4', 'rb')
    video2 = open('video/video2.mp4', 'rb')
    bot.send_message(message.chat.id, text1, parse_mode='HTML')
    time.sleep(10)
    bot.send_video(message.chat.id, video)
    bot.send_video(message.chat.id, video2)
    time.sleep(15)

    bot.send_message(message.chat.id, text2, parse_mode='HTML')
    time.sleep(10)
    photo3 = open('photo/photo3.jpg', 'rb')
    bot.send_photo(message.chat.id, photo3)
    text3 = f'''{message.from_user.first_name}, если вы здесь, то уже сделали первый шаг, и это очень смело!

    Впереди будет тест, в результате которого вы получите стратегию персонального развития:

- узнаете свои <b>сильные и слабые стороны личности</b>

- что необходимо для <b>укрепления самооценки</b>

-как выстроить фундамент жизни, где ваши <b>желания реализуются</b>

    Воплощая эту стратегию в жизнь, перемены гарантированы.

<b>Пристегните ремни, мы начинаем!</b>'''

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Здорово, поехали!')
    btn2 = types.KeyboardButton('Готовность №1, вперёд!')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text3, reply_markup=markup, parse_mode='HTML')

@bot.message_handler(commands=['comment'])
def comment(message):
    mess1 = bot.reply_to(message, 'Пожалуйста, оставьте ваш отзыв!')
    bot.register_next_step_handler(mess1, comment_action)


def comment_action(message):
    data_user = (f'ID нашего пользователя->:{message.from_user.id}, Имя нашего пользователя->:{message.from_user.first_name}, фамилия->:{message.from_user.last_name}, Ник нейм->:{message.from_user.username}')
    db_comment_save(message.from_user.id, message.text)
    c = [77777777777]
    for i in c:
        bot.send_message(i, f'У нас новый отзыв, нам написал: <b>{data_user}</b>, и вот что он пишет: <b>{message.text}</b>', parse_mode='HTML')
    text1 = ('Спасибо вам за ваш отзыв!')
    bot.send_message(message.chat.id, text1, parse_mode='HTML')



@bot.message_handler()
def get_user_text(message):
    logics(message)


if __name__ == "__main__":

    try:
        bot.polling(none_stop=True)
    except TimeoutError:
        print('Ошибка которую мы пытаемся поймать')
    finally:
        print('Сработал finally')
        time.sleep(15)
        bot.polling(none_stop=True)
        c = [77777777]
        for i in c:
            bot.send_message(i, 'ТелеграмБОТ ***** скоро упадет')



