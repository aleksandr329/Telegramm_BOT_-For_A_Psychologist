from main import *
from options import *



def logics(message):
    if message.text == 'Здорово, поехали!':
        text1 = ('''<b>Выберите вариант ответа, который наиболее Вас отражает (характеризует в большинстве случаев)</b>''')
        photo2 = open('photo/photo2.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn4 = types.KeyboardButton('В 90% случаев это про меня')
        btn5 = types.KeyboardButton('Я подолгу переживаю неудачи')
        markup.add(btn4, btn5)
        bot.send_message(message.chat.id, text1, reply_markup=markup, parse_mode='HTML')
        bot.send_photo(message.chat.id, photo2)

    elif message.text == 'Готовность №1, вперёд!':
        text1 = (
            '''<b>Выберите вариант ответа, который наиболее Вас отражает (характеризует в большинстве случаев)</b>''')
        photo2 = open('photo/photo2.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn4 = types.KeyboardButton('В 90% случаев это про меня')
        btn5 = types.KeyboardButton('Я подолгу переживаю неудачи')
        markup.add(btn4, btn5)
        bot.send_message(message.chat.id, text1, parse_mode='HTML', reply_markup=markup)
        bot.send_photo(message.chat.id, photo2)

    if message.text == 'В 90% случаев это про меня':
        photo4 = open('photo/photo4.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn6 = types.KeyboardButton('Да, я верю в свои силы ')
        btn7 = types.KeyboardButton('Конечно, справлюсь, я и по головам могу пройти ради своей цели ')
        markup.add(btn6, btn7)
        bot.send_photo(message.chat.id, photo4, reply_markup=markup)

    if message.text == 'Да, я верю в свои силы':
        photo5 = open('photo/photo5.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn8 = types.KeyboardButton('Да, я всё обдумаю и поступаю, как я считаю нужным')
        btn9 = types.KeyboardButton('Нет, я много советуюсь с другими и не пойду против мнения близких или коллег')
        markup.add(btn8, btn9)
        bot.send_photo(message.chat.id, photo5, reply_markup=markup)

    if message.text == 'Да, я всё обдумаю и поступаю, как я считаю нужным':
        photo6 = open('photo/photo6.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn10 = types.KeyboardButton('Да, для меня это вполне естественное  право иметь то, что хочешь')
        btn11 = types.KeyboardButton('Я много работаю для того, чтобы всё это иметь и мне сложно расслабиться')
        markup.add(btn10, btn11)
        bot.send_photo(message.chat.id, photo6, reply_markup=markup)

    elif message.text == 'Да, и могу доказать это каждому':
        photo6 = open('photo/photo6.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn10 = types.KeyboardButton('Да, для меня это вполне естественное  право иметь то, что хочешь')
        btn11 = types.KeyboardButton('Я много работаю для того, чтобы всё это иметь и мне сложно расслабиться')
        markup.add(btn10, btn11)
        bot.send_photo(message.chat.id, photo6, reply_markup=markup)

    if message.text == 'Да, для меня это вполне естественное  право иметь то, что хочешь':
        photo7 = open('photo/photo7.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn12 = types.KeyboardButton('Да, моё счастье – быть собой')
        btn13 = types.KeyboardButton('Я стараюсь демонстрировать своё превосходство над другими')
        markup.add(btn12, btn13)
        bot.send_photo(message.chat.id, photo7, reply_markup=markup)

    if message.text == 'Конечно, справлюсь, я и по головам могу пройти ради своей цели':
        photo8 = open('photo/photo8.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn15 = types.KeyboardButton('Да, и могу доказать это каждому')
        btn16 = types.KeyboardButton('Нет, скорее хочу, чтобы меня все считали «хорошим человеком»')
        markup.add(btn15, btn16)
        bot.send_photo(message.chat.id, photo8, reply_markup=markup)

    elif message.text == 'Если меня попросят  что-то сделать, я выполню, иногда  в ущерб себе':
        photo8 = open('photo/photo8.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn15 = types.KeyboardButton('Да, и могу доказать это каждому')
        btn16 = types.KeyboardButton('Нет, скорее хочу, чтобы меня все считали «хорошим человеком»')
        markup.add(btn15, btn16)
        bot.send_photo(message.chat.id, photo8, reply_markup=markup)

    if message.text == 'Я много работаю для того, чтобы всё это иметь и мне сложно расслабиться':
        photo13 = open('photo/photo13.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn17 = types.KeyboardButton('Нет, в конфликте я, как рыба в воде. Я часто в них побеждаю за счет подавления других')
        btn18 = types.KeyboardButton('Да, я – не конфликтный человек, стараюсь нравиться другим, а не враждовать')
        btn19 = types.KeyboardButton('Разборки не люблю, но если надо отстоять себя, то могу вступить в конфликт')
        markup.add(btn17, btn18, btn19)
        bot.send_photo(message.chat.id, photo13, reply_markup=markup)

    if message.text == 'Я подолгу переживаю неудачи':
        photo9 = open('photo/photo9.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn20 = types.KeyboardButton('Да, например, могу пройти множество обучений прежде, чем перейду к практике')
        btn21 = types.KeyboardButton('Если меня попросят  что-то сделать, я выполню, иногда  в ущерб себе')
        markup.add(btn20, btn21)
        bot.send_photo(message.chat.id, photo9, reply_markup=markup)

    if message.text == 'Да, например, могу пройти множество обучений прежде, чем перейду к практике':
        photo10 = open('photo/photo10.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn16 = types.KeyboardButton('Нет, скорее хочу, чтобы меня все считали «хорошим человеком»')
        btn22 = types.KeyboardButton('Да, обожаю, могу и похвастаться, чтобы все обалдели')
        markup.add(btn16, btn22)
        bot.send_photo(message.chat.id, photo10, reply_markup=markup)

    if message.text == 'Нет, скорее хочу, чтобы меня все считали «хорошим человеком»':
        photo11 = open('photo/photo11.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn23 = types.KeyboardButton('В целом, нет, но например, о том, что я хочу быть лидером, мне заявить страшно')
        btn24 = types.KeyboardButton('Да, я чувствую себя скованно в контакте с другими')
        markup.add(btn23, btn24)
        bot.send_photo(message.chat.id, photo11, reply_markup=markup)

    elif message.text == 'Нет, я много советуюсь с другими и не пойду против мнения близких или коллег':
        photo11 = open('photo/photo11.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn23 = types.KeyboardButton('В целом, нет, но например, о том, что я хочу быть лидером, мне заявить страшно')
        btn24 = types.KeyboardButton('Да, я чувствую себя скованно в контакте с другими')
        markup.add(btn23, btn24)
        bot.send_photo(message.chat.id, photo11, reply_markup=markup)

    if message.text == 'Да, обожаю, могу и похвастаться, чтобы все обалдели':
        photo12 = open('photo/photo12.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn25 = types.KeyboardButton('Да, при этом своих достижений всегда мало, постоянно стремлюсь к новой планке')
        btn26 = types.KeyboardButton('Я часто не знаю, чего хочу, поэтому мои достижения скромнее, чем у других')
        markup.add(btn25, btn26)
        bot.send_photo(message.chat.id, photo12, reply_markup=markup)

    elif message.text == 'В целом, нет, но например, о том, что я хочу быть лидером, мне заявить страшно':
        photo12 = open('photo/photo12.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn25 = types.KeyboardButton('Да, при этом своих достижений всегда мало, постоянно стремлюсь к новой планке')
        btn26 = types.KeyboardButton('Я часто не знаю, чего хочу, поэтому мои достижения скромнее, чем у других')
        markup.add(btn25, btn26)
        bot.send_photo(message.chat.id, photo12, reply_markup=markup)

    if message.text == 'Да, я чувствую себя скованно в контакте с другими':
        photo13 = open('photo/photo13.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn17 = types.KeyboardButton(
            'Нет, в конфликте я, как рыба в воде. Я часто в них побеждаю за счет подавления других')
        btn18 = types.KeyboardButton('Да, я – не конфликтный человек, стараюсь нравиться другим, а не враждовать')
        btn19 = types.KeyboardButton('Разборки не люблю, но если надо отстоять себя, то могу вступить в конфликт')
        markup.add(btn17, btn18, btn19)
        bot.send_photo(message.chat.id, photo13, reply_markup=markup)

    elif message.text == 'Я часто не знаю, чего хочу, поэтому мои достижения скромнее, чем у других':
        photo13 = open('photo/photo13.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn17 = types.KeyboardButton(
            'Нет, в конфликте я, как рыба в воде. Я часто в них побеждаю за счет подавления других')
        btn18 = types.KeyboardButton('Да, я – не конфликтный человек, стараюсь нравиться другим, а не враждовать')
        btn19 = types.KeyboardButton('Разборки не люблю, но если надо отстоять себя, то могу вступить в конфликт')
        markup.add(btn17, btn18, btn19)
        bot.send_photo(message.chat.id, photo13, reply_markup=markup)

    if message.text == 'Разборки не люблю, но если надо отстоять себя, то могу вступить в конфликт':
        photo14 = open('photo/photo14.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn27 = types.KeyboardButton('Рутина не так страшна, как недовольство коллег и руководства')
        btn28 = types.KeyboardButton('Да, это точно про меня')
        markup.add(btn27, btn28)
        bot.send_photo(message.chat.id, photo14, reply_markup=markup)

    elif message.text == 'Да, при этом своих достижений всегда мало, постоянно стремлюсь к новой планке':
        photo14 = open('photo/photo14.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn27 = types.KeyboardButton('Рутина не так страшна, как недовольство коллег и руководства')
        btn28 = types.KeyboardButton('Да, это точно про меня')
        markup.add(btn27, btn28)
        bot.send_photo(message.chat.id, photo14, reply_markup=markup)

    if message.text == 'Оставить коментарий 💭':
        comment(message)

    if message.text == 'Начать все сначала 🔄':
        start(message)

    if message.text == 'КОНСУЛЬТАЦИЯ':
        text = '''Консультация (онлайн или оффлайн) - 57 минут:

1 консультация - 3 000 руб.
4 консультации – 12 000 руб. 
12 консультаций – 34 000 руб. 
24 консультации – 67 000 руб.'''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn32 = types.KeyboardButton('ЗАПИСАТЬСЯ')
        btn33 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn32, btn33)
        bot.send_message(message.chat.id, text, reply_markup=markup)

    if message.text == 'ЛИЧНОЕ СОПРОВОЖДЕНИЕ':
        text = '''Личное сопровождение включает <b>консультации и дополнительную работу в телеграмм + домашние задания.</b>
Это <b>позволяет в ускоренном режиме</b> решить Ваш запрос и быстрее, чем в классической терапии, <b>прийти к желаемым результатам.</b>

1 месяц - 20 000 руб.
3 месяца – 57 000 руб.
6 месяцев – 107 000 руб.'''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn32 = types.KeyboardButton('ЗАПИСАТЬСЯ')
        btn33 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn32, btn33)
        bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode='HTML')

    if message.text == 'РАБОТА В ГРУППЕ':
        text = '''Работа в онлайн-группе по теме укрепления самооценки в течение 1 месяца. 
Стоимость - 7 000 руб.'''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn32 = types.KeyboardButton('ЗАПИСАТЬСЯ')
        btn33 = types.KeyboardButton('Начать все сначала 🔄')
        markup.add(btn32, btn33)
        bot.send_message(message.chat.id, text, reply_markup=markup)

    if message.text == 'ЗАПИСАТЬСЯ':
        z = types.InlineKeyboardMarkup()
        z.add(types.InlineKeyboardButton('Перейти в Telegram', url='https://t.me/che_katte'))
        bot.send_message(message.chat.id, 'Telegram 📲', reply_markup=z)

        ## ИТОГИ #### ИТОГИ #### ИТОГИ #### ИТОГИ #### ИТОГИ #### ИТОГИ #### ИТОГИ #### ИТОГИ #### ИТОГИ #### ИТОГИ #### ИТОГИ ##

    if message.text == 'Да, я – не конфликтный человек, стараюсь нравиться другим, а не враждовать':
        text = '''<b> «Я В ПОРЯДКЕ, ЕСЛИ РАДУЮ ДРУГИХ»
Ваша самооценка зависит от одобрения и принятия со стороны окружающих. А чтобы это одобрение получить, Вы считаете, что 
должны соответствовать ожиданиям других людей.

Вы постоянно сдерживаете свои  чувства, Вам крайне сложно отстаивать свои интересы и делать что-то для себя. 

Не знаете, чего хотите и как будто совсем нет энергии. Не верите, что можете добиться существенных успехов.</b>'''

        bot.send_message(message.chat.id, text, parse_mode='HTML')
        time.sleep(10)
        video3 = open('video/video3.mp4', 'rb')
        bot.send_video(message.chat.id, video3)
        time.sleep(15)
        text2 = '''Персональная стратегия для укрепления самооценки: 

<b>• Начните радовать себя:</b>

ваш фокус внимания в основном на других, верните его на себя. Вспомните, что доставляет  радость именно вам и наполните этим свою жизнь!
 
Попробуйте в качестве эксперимента культивировать своё «хочу» и посмотрите, как преобразиться ваша жизнь!


<b>• Восстановите эмоциональную сферу:</b>

• необходимо проживать эмоции, а не подавлять их в себе! Это тот шаг, который высвободит много энергии, которая раньше шла на подавление. 

<b>• Отстаивайте свои интересы:</b>

быть самым главным человеком в своей жизни – это большая смелость, которая даёт возможность отстаивать себя и свои интересы!
 Учитесь этому и делайте маленькие шаги в данном направлении. 
<b>• Учитесь просить о помощи:</b>

Вы привыкли всё делать самостоятельно, чтобы никого не напрягать. Попробуйте сделать иначе – попросите близких о помощи 
и увидите, как это облегчит вашу жизнь!

<b>• Планируйте свою жизнь:</b>

Подстраиваясь каждый раз под других людей, очень сложно жить собственную жизнь. Постройте планы на ближайшую неделю и придерживайтесь их!'''
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        time.sleep(15)
        video4 = open('video/video4.mp4', 'rb')
        bot.send_video(message.chat.id, video4)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn29 = types.KeyboardButton('КОНСУЛЬТАЦИЯ')
        btn30 = types.KeyboardButton('ЛИЧНОЕ СОПРОВОЖДЕНИЕ')
        btn31 = types.KeyboardButton('РАБОТА В ГРУППЕ')
        btn32 = types.KeyboardButton('Начать все сначала 🔄')
        btn33 = types.KeyboardButton('Оставить коментарий 💭')
        markup.add(btn29, btn30, btn31, btn32, btn33)
        bot.send_message(message.chat.id, '👇', reply_markup=markup)

    elif message.text == 'Рутина не так страшна, как недовольство коллег и руководства':
        text = '''<b> «Я В ПОРЯДКЕ, ЕСЛИ РАДУЮ ДРУГИХ»
Ваша самооценка зависит от одобрения и принятия со стороны окружающих. А чтобы это одобрение получить, Вы считаете, что 
должны соответствовать ожиданиям других людей.

Вы постоянно сдерживаете свои  чувства, Вам крайне сложно отстаивать свои интересы и делать что-то для себя. 

Не знаете, чего хотите и как будто совсем нет энергии. Не верите, что можете добиться существенных успехов.</b>'''

        bot.send_message(message.chat.id, text, parse_mode='HTML')
        time.sleep(10)
        video3 = open('video/video3.mp4', 'rb')
        bot.send_video(message.chat.id, video3)
        time.sleep(15)
        text2 = '''Персональная стратегия для укрепления самооценки: 

<b>• Начните радовать себя:</b>

ваш фокус внимания в основном на других, верните его на себя. Вспомните, что доставляет  радость именно вам и наполните этим свою жизнь! 

Попробуйте в качестве эксперимента культивировать своё «хочу» и посмотрите, как преобразиться ваша жизнь!

<b>• Восстановите эмоциональную сферу:</b>

• необходимо проживать эмоции, а не подавлять их в себе! Это тот шаг, который высвободит много энергии, которая раньше шла на подавление.
 
<b>• Отстаивайте свои интересы:</b>

быть самым главным человеком в своей жизни – это большая смелость, которая даёт возможность отстаивать себя и свои интересы!
Учитесь этому и делайте маленькие шаги в данном направлении.
  
<b>• Учитесь просить о помощи:</b>

Вы привыкли всё делать самостоятельно, чтобы никого не напрягать. Попробуйте сделать иначе – попросите близких о помощи 
и увидите, как это облегчит вашу жизнь!

<b>• Планируйте свою жизнь:</b>

Подстраиваясь каждый раз под других людей, очень сложно жить собственную жизнь. Постройте планы на ближайшую неделю и придерживайтесь их!'''
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        time.sleep(15)
        video4 = open('video/video4.mp4', 'rb')
        bot.send_video(message.chat.id, video4)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn29 = types.KeyboardButton('КОНСУЛЬТАЦИЯ')
        btn30 = types.KeyboardButton('ЛИЧНОЕ СОПРОВОЖДЕНИЕ')
        btn31 = types.KeyboardButton('РАБОТА В ГРУППЕ')
        btn32 = types.KeyboardButton('Начать все сначала 🔄')
        btn33 = types.KeyboardButton('Оставить коментарий 💭')
        markup.add(btn29, btn30, btn31, btn32, btn33)
        bot.send_message(message.chat.id, '👇', reply_markup=markup)

    if message.text == 'Нет, в конфликте я, как рыба в воде. Я часто в них побеждаю за счет подавления других':
        text = '''<b> «Я В ПОРЯДКЕ, ЕСЛИ Я – СИЛЬНАЯ(ЫЙ)»
Презираете проявление слабости в других, и не признаёте её в себе, предпочитая надевать маску «сильного человека». Не 
поддаётесь давлению, не признаёте ошибок и не доверяете людям.

Вы бываете жестоки, часто игнорируете свои и чужие чувства, склонны перекладывать вину на других.</b>'''

        bot.send_message(message.chat.id, text, parse_mode='HTML')
        time.sleep(10)
        video3 = open('video/video3.mp4', 'rb')
        bot.send_video(message.chat.id, video3)
        time.sleep(15)
        text2 = '''Персональная стратегия для укрепления самооценки: 

<b>• Расслабьтесь:</b>
 
Вы много сил тратите на доказательство своей силы. Если принимать себя такой, как есть, со всеми плюсами и минусами, это 
позволит избежать лишнего напряжения.

<b>• Принятие собственных эмоций:</b>
 
Испытывать грусть, страх, скуку, волнения, жалость – это нормально для всех людей. Без этих эмоций спектр ощущений 
человека неполноценен, поэтому необходимо разрешать себе в них погружаться.

<b>• Общаясь с людьми, старайтесь больше слушать, чем говорить:</b>

Это позволит вам лучше понимать окружающих, их логику мыслей и мотивы поведения, а следовательно, откроет путь к взаимопониманию.
 
<b>• Рассматривайте людей с позиции выявления особенностей, а не слабостей:</b>

У всех людей есть сильные и слабые стороны, вы обычно концентрируетесь на минусах окружающих. Попробуйте посмотреть 
более объёмно на мир: у каждой медали замечайте сразу две стороны. 
    '''
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        time.sleep(15)
        video4 = open('video/video4.mp4', 'rb')
        bot.send_video(message.chat.id, video4)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn29 = types.KeyboardButton('КОНСУЛЬТАЦИЯ')
        btn30 = types.KeyboardButton('ЛИЧНОЕ СОПРОВОЖДЕНИЕ')
        btn31 = types.KeyboardButton('РАБОТА В ГРУППЕ')
        btn32 = types.KeyboardButton('Начать все сначала 🔄')
        btn33 = types.KeyboardButton('Оставить коментарий 💭')
        markup.add(btn29, btn30, btn31, btn32, btn33)
        bot.send_message(message.chat.id, '👇', reply_markup=markup)

    elif message.text == 'Я стараюсь демонстрировать своё превосходство над другими':
        text = '''<b> «Я В ПОРЯДКЕ, ЕСЛИ Я – СИЛЬНАЯ(ЫЙ)»
Презираете проявление слабости в других, и не признаёте её в себе, предпочитая надевать маску «сильного человека». Не 
поддаётесь давлению, не признаёте ошибок и не доверяете людям.

Вы бываете жестоки, часто игнорируете свои и чужие чувства, склонны перекладывать вину на других.</b>'''

        bot.send_message(message.chat.id, text, parse_mode='HTML')
        time.sleep(10)
        video3 = open('video/video3.mp4', 'rb')
        bot.send_video(message.chat.id, video3)
        time.sleep(15)
        text2 = '''Персональная стратегия для укрепления самооценки: 

<b>• Расслабьтесь:</b>
 
Вы много сил тратите на доказательство своей силы. Если принимать себя такой, как есть, со всеми плюсами и минусами, это 
позволит избежать лишнего напряжения.

<b>• Принятие собственных эмоций:</b> 

Испытывать грусть, страх, скуку, волнения, жалость – это нормально для всех людей. Без этих эмоций спектр ощущений 
человека неполноценен, поэтому необходимо разрешать себе в них погружаться.

<b>• Общаясь с людьми, старайтесь больше слушать, чем говорить:</b>

Это позволит вам лучше понимать окружающих, их логику мыслей и мотивы поведения, а следовательно, откроет путь к взаимопониманию.
 
<b>• Рассматривайте людей с позиции выявления особенностей, а не слабостей:</b>

У всех людей есть сильные и слабые стороны, вы обычно концентрируетесь на минусах окружающих. Попробуйте посмотреть более объёмно на мир: у каждой медали замечайте сразу две стороны.'''
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        time.sleep(15)
        video4 = open('video/video4.mp4', 'rb')
        bot.send_video(message.chat.id, video4)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn29 = types.KeyboardButton('КОНСУЛЬТАЦИЯ')
        btn30 = types.KeyboardButton('ЛИЧНОЕ СОПРОВОЖДЕНИЕ')
        btn31 = types.KeyboardButton('РАБОТА В ГРУППЕ')
        btn32 = types.KeyboardButton('Начать все сначала 🔄')
        btn33 = types.KeyboardButton('Оставить коментарий 💭')
        markup.add(btn29, btn30, btn31, btn32, btn33)
        bot.send_message(message.chat.id, '👇', reply_markup=markup)

    if message.text == 'Да, моё счастье – быть собой':
        text = '''<b>СТАБИЛЬНАЯ САМООЦЕНКА
Ваше ощущение себя не зависит от внешних обстоятельств. Можете сориентироваться в изменчивой реальность, при этом оставаясь спокойным и практичным человеком.</b>'''

        text2 = '''<b>У ВАС УЖЕ ХОРОШИЙ ФУНДАМЕНТ для достижения ваших целей и желаний.</b> Иногда для того, чтобы 
<b>жить собственной жизнью</b> надо немного поработать. 
        
Например, научиться выражать агрессию, чтобы управлять своими границами и <b>проявлять любовь.</b> Познакомиться 
поближе со стыдом и виной, чтобы строить <b>здоровые отношения с собой и окружающими.</b> 

Я помогаю клиенту выбирать <b>в жизни то, что ему важно,</b> но по каким-то причинам сложно. Осознать эти причины, 
сделать их явными и <b>найти способ получения желаемого</b> - это красивый психотерапевтический процесс, в котором я сопровождаю клиента!

Форматы дальнейшей работы со мной:'''
        bot.send_message(message.chat.id, text, parse_mode='HTML')
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn29 = types.KeyboardButton('КОНСУЛЬТАЦИЯ')
        btn30 = types.KeyboardButton('ЛИЧНОЕ СОПРОВОЖДЕНИЕ')
        btn31 = types.KeyboardButton('РАБОТА В ГРУППЕ')
        btn32 = types.KeyboardButton('Начать все сначала 🔄')
        btn33 = types.KeyboardButton('Оставить коментарий 💭')
        markup.add(btn29, btn30, btn31, btn32, btn33)
        bot.send_message(message.chat.id, '👇', reply_markup=markup)

    if message.text == 'Да, это точно про меня':
        text = '''<b>«Я В ПОРЯДКЕ, ЕСЛИ Я – ЛУЧШЕ ОСТАЛЬНЫХ»
Вы оцениваете себя исключительно через призму своих достижений и всегда сравниваете себя с другими, часто не в свою пользу. 

Быстро загораетесь идеей и потом бросаете, не доведя дело до конца. Ждёте идеального момента, чтобы начать новое дело, кажется, что «я недостаточно готов».

Вы – чувствительный человек.</b>'''

        bot.send_message(message.chat.id, text, parse_mode='HTML')
        time.sleep(10)
        video3 = open('video/video3.mp4', 'rb')
        bot.send_video(message.chat.id, video3)
        time.sleep(15)
        text2 = '''Персональная стратегия для укрепления самооценки: 

<b>• Перестаньте сравнивать себя с другими:</b>
 
Каждый человек уникален, и в тоже время всегда есть кто-то быстрее, выше, сильнее вас – это бесконечная гонка. Обратите 
внимание на СВОИ цели, желания, особенности, раскрывайте их и наслаждайтесь собой без сравнения с остальным миром.
 
<b>• Научитесь доводить дела до конца:</b>

Возьмите ответственность за результат и приходите к нему самостоятельно или работая в команде, возможно делегируя часть обязанностей. 
<b>• Перестаньте ранжировать людей на тех, кто «хуже» или «лучше» вас:</b>

Посмотрите на ваше окружение, как на людей с их чувствами, эмоциями, переживаниями. Ведь достижения, это только часть 
жизни, есть ещё и более тонкие планы. Рассмотреть в человеке – Человека, вот главная задача! Обращая внимание на этот 
аспект, вы перестанете воспринимать людей как «функцию» или «шкалу достижений», по которой равняете и себя.

<b>• Мотивация и цель:</b>

Когда начинаете новое дело, на берегу определитель с той целью, ради которой это дело затеваете. В те моменты, когда 
захочется всё бросить, вспоминайте и мотивируйте себя, тогда довести дело до конца будет намного легче.'''
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
        time.sleep(15)
        video4 = open('video/video4.mp4', 'rb')
        bot.send_video(message.chat.id, video4)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn29 = types.KeyboardButton('КОНСУЛЬТАЦИЯ')
        btn30 = types.KeyboardButton('ЛИЧНОЕ СОПРОВОЖДЕНИЕ')
        btn31 = types.KeyboardButton('РАБОТА В ГРУППЕ')
        btn32 = types.KeyboardButton('Начать все сначала 🔄')
        btn33 = types.KeyboardButton('Оставить коментарий 💭')
        markup.add(btn29, btn30, btn31, btn32, btn33)
        bot.send_message(message.chat.id, '👇', reply_markup=markup)
















