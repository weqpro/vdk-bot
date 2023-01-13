import telebot


def log_con(message: telebot.types.Message):
    print(f"{message.from_user.first_name}: \"{message.text}\"")
