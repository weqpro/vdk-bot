from telebot import TeleBot
import functions
from data import DefaultValues
import log

bot = TeleBot("5929593455:AAGtDmOZGaU67WXfNaTlEnhFtwfK3hx4LVU", parse_mode='Markdown')


@bot.message_handler(func=lambda m: m.text in DefaultValues.commands.keys())
def process_commands(message):
    func = getattr(functions, DefaultValues.commands[message.text])
    func(message, bot)


@bot.message_handler(func=lambda m: True)
def non_process(message):
    bot.reply_to(message, "Введіть команду /start")
    log.log_con(message)


bot.polling(none_stop=True)
