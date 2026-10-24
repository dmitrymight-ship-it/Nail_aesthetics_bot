import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_start(message):
    bot.reply_to(message, '_')


@bot.message_handler(func=lambda message: True)
def question(message):
    bot.reply_to(message, f'''Такой команды нет: {message.text}.
    Попробуйте воспользоваться командой /start или /help''')


bot.polling()
