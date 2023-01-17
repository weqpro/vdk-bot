import datetime
import re
import os
import data
import log
from telebot import types, TeleBot


path = "D:\PokazyTG"


def submit(message: types.Message, bot: TeleBot):
    bot.send_message(message.chat.id, "*Для подачі показника введіть будь-ласка Вашу Адресу, ос.рахунок:сам показник.*")
    bot.send_message(message.chat.id,
                     "Наприклад:\n\n"
                     "*Шевченко Т.Г.:Світла 7б:153*")
    log.log_con(message)

    bot.register_next_step_handler(message, process_name_step, bot)


def process_name_step(message: types.Message, bot: TeleBot):
    f = open(path + '\\' + str(datetime.datetime.fromtimestamp(message.date))[:-9] + '.txt', 'a+')
    f.write(message.text + '\n')

    bot.send_message(message.chat.id, "Дякую, ваш показник прийнято")

    log.log_con(message)


def help(message: types.Message, bot: TeleBot):
    bot.reply_to(message, "Для подачі показів можна використовувати цей бот, або номера телефонів нижче")
    bot.send_message(message.chat.id, "+++ (123)")
    bot.send_message(message.chat.id, "032-295-05-55 (Стаціонарний)")
    log.log_con(message)


def start(message: types.Message, bot: TeleBot):
    data.DefaultValues.users.append(message.chat.id)

    bot.send_message(message.chat.id, "Ласкаво просимо до боту для подачі показів Вододканал Зимна Вода")
    bot.send_message(message.chat.id, "для того, щоб подати показ напишіть команду /podaty", reply_markup=main_menu_keyboard())


def info(message: types.Message, bot: TeleBot):
    if message.chat.id in data.DefaultValues.users:
        data.DefaultValues.users.remove(message.chat.id)
        bot.send_message(message.chat.id, "Ви відписані від розсилики")
    else:
        data.DefaultValues.users.append(message.chat.id)
        bot.send_message(message.chat.id, "Ви підписані на розсилку від адміністрації")


def send_info(message: types.Message, bot: TeleBot):
    if message.from_user.id in data.DefaultValues.admins:
        bot.send_message(message.chat.id, "Що написати?")
    else:
        bot.send_message(message.chat.id, "У вас недостатньо прав на цю команду")

    bot.register_next_step_handler(message, process_info_step, bot)


def process_info_step(message: types.Message, bot: TeleBot):
    inf = message.text

    for u in data.DefaultValues.users:
        bot.send_message(u, inf)

    bot.send_message(message.chat.id, "Виконано!")


def information(message: types.Message, bot: TeleBot):
    bot.send_message(message.chat.id, "Водоканал Зимна Вода вул. Шептицького 5")
    bot.send_message(message.chat.id, "Графік:\n\nбудні дні: 9:00-17:00")
    bot.send_message(message.chat.id, "Тариф:\n\nВодовідведення: 10,14\nВода:19.92")
    bot.send_message(message.chat.id, "Номер конролера: 0677506811 - Володомир")


def emergency(message: types.Message, bot: TeleBot):
    bot.send_message(message.chat.id, "У разі витоку каналізації або проривуна водогоні повідмте на номер 0636222468")


def main_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.InlineKeyboardButton(text="Повідомити про аварію", callback_data='send_info'), types.InlineKeyboardButton(text="Подати показник", callback_data='meter'))
    keyboard.add(types.InlineKeyboardButton(text="Інформація для споживачів", callback_data='lang'))
    return keyboard