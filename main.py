# Бот для генерации игр
import telebot
from telebot import types
import random
import time
import cowsay

while True:
    try:
        cowsay.cow('Bot started...')
        bot = telebot.TeleBot('6104388060:AAGuE2Kcqh49lzl-qyYPdofFrdsOK8htv0g')

        # Создание клавиатур
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        kb_timing = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        kb_exit = types.ReplyKeyboardMarkup(resize_keyboard=True)
        kb_random = types.ReplyKeyboardMarkup(resize_keyboard=True)
        kb_random_timing = types.ReplyKeyboardMarkup(resize_keyboard=True)
        kb_other = types.InlineKeyboardMarkup()
        kb_other_m = types.InlineKeyboardMarkup()
        kb_other_time = types.InlineKeyboardMarkup()

        # Создание кнопок
        games = types.InlineKeyboardButton(text='Случайная игра 🎰')
        members = types.InlineKeyboardButton(text='Количество игроков 👨‍👩‍👧‍👦')
        timing = types.InlineKeyboardButton(text='Выбрать продолжительность 🕰️')
        fast = types.InlineKeyboardButton(text='Быстрая 🏃')
        middle = types.InlineKeyboardButton(text='Средняя 🚶')
        longest = types.InlineKeyboardButton(text='Долгая 🧑‍🦽')
        exit = types.InlineKeyboardButton(text='Вернуться в начало 🔙')
        other = types.InlineKeyboardButton(text="Меняй🔄", callback_data='other')
        other_m = types.InlineKeyboardButton(text="Меняй🔄", callback_data='other_game_m')
        other_time = types.InlineKeyboardButton(text="Меняй🔄", callback_data='other_game_time')


        kb.add(games, timing)
        kb_timing.add(fast, middle, longest, members)
        kb_random.add(games)
        kb_random_timing.add(members, games)
        kb_exit.add(exit)
        kb_other.add(other)
        kb_other_m.add(other_m)
        kb_other_time.add(kb_other_time)

        games = [
            ["Гарри Поттер", 1, 5, "Долгая 🧑‍🦽"],
            ['Гравити Фоллз', 1, 5, "Долгая 🧑‍🦽"],
            ['Ужас Аркхэма', 1, 6, 'Долгая 🧑‍🦽'],
            ['Exit', 1, 99, 'Долгая 🧑‍🦽'],
            ['Клаустрофобия', 1, 99, 'Долгая 🧑‍🦽'],
            ['Дженга', 1, 99, 'Средняя 🚶'],
            ['Побег из психушки', 1, 99, 'Долгая 🧑‍🦽'],
            ["Карточные войны", 2, 2, "Средняя 🚶"],
            ["Запретный остров", 2, 4, "Средняя 🚶"],
            ["Колонизаторы", 2, 4, "Средняя 🚶"],
            ["Челюсти", 2, 4, "Средняя 🚶"],
            ["Шакал", 2, 4, "Долгая 🧑‍🦽"],
            ["Эволюция. Случайные мутации", 2, 4, "Средняя 🚶"],
            ["Каркассон", 2, 5, "Долгая 🧑‍🦽"],
            ["Рик и морти. Всмортить всё", 2, 5, "Средняя 🚶"],
            ["Монополия", 2, 6, "Долгая 🧑‍🦽"],
            ["Эпичные схватки боевых магов", 2, 6, "Долгая 🧑‍🦽"],
            ["Цитадели", 2, 7, "Средняя 🚶"],
            ["Зельеварение", 2, 8, "Долгая 🧑‍🦽"],
            ["Эволюция", 2, 8, "Долгая 🧑‍🦽"],
            ["Свинтус 2.0", 2, 10, "Быстрая 🏃"],
            ["Свинтус. Злоключения", 2, 10, "Быстрая 🏃"],
            ["Свинтус мини", 2, 10, "Быстрая 🏃"],
            ["Соображарий", 2, 10, "Средняя 🚶"],
            ["Суперсоображарий", 2, 10, "Средняя 🚶"],
            ["Манчкин. Ктулху", 3, 6, "Средняя 🚶"],
            ["Манчкин. Гравити Фолз", 3, 6, "Средняя 🚶"],
            ["Хугермугер", 3, 10, "Средняя 🚶"],
            ["Крокодил", 3, 16, "Средняя 🚶"],
            ["За бортом", 4, 6, "Долгая 🧑‍🦽"],
            ["Диксит", 4, 7, "Долгая 🧑‍🦽"],
            ["Имаджинариум", 4, 7, "Долгая 🧑‍🦽"],
            ["Страдающее средневековье", 4, 9, "Долгая 🧑‍🦽"],
            ["Нечто", 4, 12, "Средняя 🚶"],
            ["Alias", 4, 98, "Средняя 🚶"],
            ["Мафия", 6, 16, "Средняя 🚶"]
        ]

        ch_games = []

        # Функция вывода игры по игрокам
        def get_game(players):
            ch_games = []
            for game in games:
                if game[1] <= int(players) <= game[2]:
                    ch_games.append(game[0])
            if len(ch_games) > 0:
                return random.choice(ch_games)
            else:
                return None

        # Функция вывода игры по продолжительности и игрокам
        def get_game_time(value, players):
            ch_games = []
            for game in games:
                if game[3] == value:
                    if int(game[1]) <= int(players) <= int(game[2]):
                        ch_games.append(game)
            if len(ch_games) > 0:
                return random.choice(ch_games)
            else:
                return None

        result = ch_games

        # Обработчик команды /start
        @bot.message_handler(commands=['start'])
        def start(message):
            bot.send_message(message.chat.id, f'Привет, {message.from_user.username}! '
                                              f'\nЗдесь ты можешь подобрать случайную игру по своим критериям.'
                                              f'\nС помощью кнопок клавиатуры сделай свой выбор!', reply_markup=kb)


        @bot.callback_query_handler(func=lambda call: call.data in ['other', 'other_game_m', 'other_game_time'])
        def other_game(call):
            global result
            if call.data == 'other':
                game = random.choice(games)
                game_rand = open(f'game_pictures/{game[0]}.jpg', 'rb')
                bot.send_photo(call.message.chat.id, game_rand, f'<u>{game[0]}</u>', parse_mode='html', reply_markup=kb_other)
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            elif call.data == 'other_game_m':
                game = random.choice(result)
                pic = open(f'game_pictures/{game}.jpg', 'rb')
                bot.send_photo(call.message.chat.id, pic, f'<u>{game}</u>', parse_mode='html',
                               reply_markup=kb_other_m)
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            elif call.data == 'other_game_time':
                game = random.choice(result)
                pic = open(f'game_pictures/{game}.jpg', 'rb')
                bot.send_photo(call.message.chat.id, pic, f'<u>{game}</u>', parse_mode='html',
                               reply_markup=kb_other_time)
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)



        # Обработчик кнопки Случайная игра
        @bot.message_handler(func=lambda message: message.text == 'Случайная игра 🎰')
        def random_game(message):
            game = random.choice(games)
            game_pic = open(f'game_pictures/{game[0]}.jpg', 'rb')
            bot.send_message(message.chat.id, 'Твоя игра: ', parse_mode='html',
                             reply_markup=kb_exit)
            bot.send_photo(message.chat.id, game_pic, f'<u>{game[0]}</u>', parse_mode='html', reply_markup=kb_other)


        # Обработчик кнопки Продолжительность игры
        @bot.message_handler(func=lambda message: message.text == 'Выбрать продолжительность 🕰️')
        def choice_timing(message):
            bot.send_message(message.chat.id, f'{message.from_user.username}, выбери продолжительность игры! '
                                              f'\n'
                                              f'\n<u>Небольшая памятка</u>:'
                                              f'\n<b>Быстрая 🏃</b> - до 30 минут;'
                                              f'\n<b>Средняя 🚶</b> - от 30 до 60 минут;'
                                              f'\n<b>Долгая 🧑‍🦽</b> от 60 минут\n'
                                              f'\nЛибо можешь нажать на количество игроков!', parse_mode='html',
                             reply_markup=kb_timing)
            bot.register_next_step_handler(message, time_game)


        # Обработчик кнопoк Быстрая, Средняя, Долгая
        def time_game(message):
            ph_choice = open('img/choice.jpeg', 'rb')
            value = message.text
            if any(keyword in value for keyword in ["Быстрая 🏃", "Средняя 🚶", "Долгая 🧑‍🦽"]):
                bot.send_photo(message.chat.id, ph_choice,
                               f'Введи количество игроков или можешь выбрать случайную игру',
                               reply_markup=kb_random_timing)
                bot.register_next_step_handler(message, lambda msg: duration_players_input(msg, value))
            elif message.text == 'Количество игроков 👨‍👩‍👧‍👦':
                ph_pl = open('img/players.jpeg', 'rb')
                bot.send_photo(message.chat.id, ph_pl, 'Введи количество игроков:')
                bot.register_next_step_handler(message, lambda msg: get_members(msg, ))
            else:
                bot.send_message(message.chat.id,
                                 'Что-то пошло не так. Попробуй ещё раз, либо можешь вернуться в начало',
                                 reply_markup=kb_exit)
                bot.register_next_step_handler(message, start)


        def duration_players_input(message, value):
            if message.text == 'Случайная игра 🎰':
                game = get_game_time(value)
                game_pic = open(f'game_pictures/{game[0]}.jpg', 'rb')
                if game is not None:
                    bot.send_message(message.chat.id, 'Твоя игра: ', parse_mode='html',
                                     reply_markup=kb_exit)
                    bot.send_photo(message.chat.id, game_pic, f'<u>{game[0]}</u>', parse_mode='html', reply_markup=kb_other)
                else:
                    pepe = open('img/pepe.jpg', 'rb')
                    bot.send_photo(message.chat.id, pepe, 'Игру не удалось подобрать.',
                                     reply_markup=kb_exit)
            else:
                try:
                    players = int(message.text.strip())
                    if players > 0:
                        game = get_game_time(value, players)
                        if game is not None:
                            pic = open(f'game_pictures/{game[0]}.jpg', 'rb')
                            bot.send_message(message.chat.id, 'Твоя игра: ', parse_mode='html',
                                             reply_markup=kb_exit)
                            bot.send_photo(message.chat.id, pic, f'<u>{game[0]}</u>', parse_mode='html', reply_markup=kb_other_time)
                        else:
                            pepe = open('img/pepe.jpg', 'rb')
                            bot.send_photo(message.chat.id, pepe, 'Игру не удалось подобрать.',
                                           reply_markup=kb_exit)

                except ValueError:
                    ph_pl = open('img/players.jpeg', 'rb')
                    bot.send_photo(message.chat.id, ph_pl, 'Введи количество игроков:')
                    bot.register_next_step_handler(message, lambda msg: duration_players_input(msg, value))


        # Обработчик кнопки Количество игроков
        @bot.message_handler(func=lambda message: message.text == 'Количество игроков 👨‍👩‍👧‍👦')
        def members(message):
            ph_pl = open('img/players.jpeg', 'rb')
            bot.send_photo(message.chat.id, ph_pl, 'Введи количество игроков:')
            bot.register_next_step_handler(message, get_members)


        def get_members(message):
            players = int(message.text)
            game_ch = get_game(players)
            if game_ch:
                game_pic = open(f'game_pictures/{game_ch}.jpg', 'rb')
                bot.send_message(message.chat.id, 'Твоя игра: ', parse_mode='html',
                                 reply_markup=kb_exit)
                bot.send_photo(message.chat.id, game_pic, f'<u>{game_ch}</u>', parse_mode='html', reply_markup=kb_other_m)
            else:
                pepe = open('img/pepe.jpg', 'rb')
                bot.send_photo(message.chat.id, pepe, 'Игру не удалось подобрать.',
                                     reply_markup=kb_exit)



        # Возврат в начало
        @bot.message_handler(func=lambda message: message.text == 'Вернуться в начало 🔙')
        def restart(message):
            bot.send_message(message.chat.id, "Вы вернулись в начало. "
                                              "\nБудь лапочкой, ударь по кнопке ☺", reply_markup=kb)


        # Обработчик лишних слов, не по делу
        @bot.message_handler(func=lambda message: message.text != ['Случайная игра 🎰', 'Количество игроков 👨‍👩‍👧‍👦',
                                                                   'Выбрать продолжительность 🕰️', 'Быстрая 🏃',
                                                                   'Средняя 🚶', 'Долгая 🧑‍🦽', 'Вернуться в начало 🔙'])
        def exception(message):
            photo = open('img/ditch.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, 'Ты втираешь какую-то дичь. \nВернись в меню', reply_markup=kb_exit)


        bot.polling(none_stop=True)
    except Exception as e:
        print('Error: ', e)
        print('Bot restart...')
        time.sleep(5)