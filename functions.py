import datetime
import re
import log
from telebot import types, TeleBot


path ="D:\PokazyTG"
r = re.compile('.*/.*/.*:.*')


def send_welcome(message: types.Message, bot: TeleBot):
    bot.reply_to(message, "Вас вітає бот для подачі показників Водоканал Зимна Вода")
    bot.send_message(message.chat.id, "*Для подачі показника введіть будь-ласка Вашу Адресу, ос.рахунок:сам показник.*")
    bot.send_message(message.chat.id,
                     "Наприклад:\n\n"
                     "*Нагурський Р.С.:Барановського,7:153*")
    log.log_con(message)

    bot.register_next_step_handler(message, process_name_step, bot)


def process_name_step(message: types.Message, bot: TeleBot):
    f = open(path + '\\' + str(datetime.datetime.fromtimestamp(message.date))[:-9] + '.txt', 'a+')
    f.write(message.text + '\n')

    bot.send_message(message.chat.id, "Дякую, ваш показник прийнято")

    log.log_con(message)
