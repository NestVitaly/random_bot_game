# Бот для генерации игр
import telebot
from telebot import types
import random
import time

while True:
    try:
        print('Bot started...')
        bot = telebot.TeleBot('6104388060:AAGuE2Kcqh49lzl-qyYPdofFrdsOK8htv0g')

        # Создание клавиатур
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        kb_timing = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        kb_exit = types.ReplyKeyboardMarkup(resize_keyboard=True)
        kb_random = types.ReplyKeyboardMarkup(resize_keyboard=True)
        kb_random_timing = types.ReplyKeyboardMarkup(resize_keyboard=True)

        # Создание кнопок
        games = types.InlineKeyboardButton(text='Случайная игра 🎰')
        members = types.InlineKeyboardButton(text='Количество игроков 👨‍👩‍👧‍👦')
        timing = types.InlineKeyboardButton(text='Выбрать продолжительность 🕰️')
        fast = types.InlineKeyboardButton(text='Быстрая 🏃')
        middle = types.InlineKeyboardButton(text='Средняя 🚶')
        longest = types.InlineKeyboardButton(text='Долгая 🧑‍🦽')
        exit = types.InlineKeyboardButton(text='Вернуться в начало 🔙')

        kb.add(games, members, timing)
        kb_timing.add(fast, middle, longest)
        kb_random.add(games)
        kb_random_timing.add(members, games)
        kb_exit.add(exit)


        games = [
            ["Гарри Поттер", 1, 5, "Долгая 🧑‍🦽"],
            ['Гравити Фоллз', 1, 5, "Долгая 🧑‍🦽"],
            ['Ужас Аркхэма', 1, 6, 'Долгая 🧑‍🦽'],
            ['Exit', 1, 99, 'Долгая 🧑‍🦽'],
            ['Клаустрофобия', 1, 99, 'Долгая 🧑‍🦽'],
            ['Дженга', 1, 99, 'Средняя 🚶'],
            ['Побег из психушки', 1, 99, 'Долгая 🧑‍🦽']
        ]


        # Функция вывода игры по игрокам
        def get_game(players):
            ch_games = []
            for game in games:
                if game[1] <= players <= game[2]:
                    ch_games.append(game[0])
            if len(ch_games) > 0:
                return random.choice(ch_games)
            else:
                return None


        # Функция вывода игры по продолжительности и игрокам
        def get_game_time(value, players=None):
            ch_games = []
            for game in games:
                if game[3] == value:
                    if (players is None) or (game[1] <= players <= game[2]):
                        ch_games.append(game)
            if len(ch_games) > 0:
                return random.choice(ch_games)
            else:
                return None


        # Обработчик команды /start
        @bot.message_handler(commands=['start'])
        def start(message):
            bot.send_message(message.chat.id, f'Привет, {message.from_user.username}! '
                                              f'\nЗдесь ты можешь подобрать случайную игру по своим критериям.'
                                              f'\nС помощью кнопок клавиатуры сделай свой выбор!', reply_markup=kb)


        # Обработчик кнопки Случайная игра
        @bot.message_handler(func=lambda message: message.text == 'Случайная игра 🎰')
        def random_game(message):
            game = random.choice(games)
            bot.send_message(message.chat.id, f'Твоя случайная игра: <u>{game[0]}</u>', parse_mode='html',
                             reply_markup=kb_exit)


        # Обработчик кнопки Продолжительность игры
        @bot.message_handler(func=lambda message: message.text == 'Выбрать продолжительность 🕰️')
        def choice_timing(message):
            bot.send_message(message.chat.id, f'{message.from_user.username}, выбери продолжительность игры! '
                                              f'\n'
                                              f'\n<u>Небольшая памятка</u>:'
                                              f'\n<b>Быстрая 🏃</b> - до 30 минут;'
                                              f'\n<b>Средняя 🚶</b> - от 30 до 60 минут;'
                                              f'\n<b>Долгая 🧑‍🦽</b> от 60 минут', parse_mode='html',
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
            else:
                bot.send_message(message.chat.id,
                                 'Что-то пошло не так. Попробуй ещё раз, либо можешь вернуться в начало',
                                 reply_markup=kb_exit)
                bot.register_next_step_handler(message, start)


        def duration_players_input(message, value):
            if message.text == 'Случайная игра 🎰':
                game = get_game_time(value)
                if isinstance(game, list):
                    bot.send_message(message.chat.id, f'Твоя игра: <u>{game[0]}</u>', parse_mode='html',
                                     reply_markup=kb_exit)
                else:
                    bot.send_message(message.chat.id, 'Игру не удалось подобрать, Вам очень грустно.',
                                     reply_markup=kb_exit)
            else:
                try:
                    players = int(message.text.strip())
                    if players > 0:
                        game = get_game_time(value, players)
                        if game is not None:
                            bot.send_message(message.chat.id, f'Вот твоя игра: <u>{game[0]}</u>', parse_mode='html',
                                             reply_markup=kb_exit)
                        else:
                            bot.send_message(message.chat.id, 'Игру не удалось подобрать, Вам очень грустно.',
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
                bot.send_message(message.chat.id, f'Твоя игра: <u>{game_ch}</u>', parse_mode='html',
                                 reply_markup=kb_exit)
            else:
                bot.send_message(message.chat.id, 'Болты, игра не найдена.', reply_markup=kb_exit)


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