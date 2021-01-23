import telebot
from config import token,user_id

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(user_id, "A human?!")

@bot.message_handler(content_types=['text'])
def send_greetings(message):
    if "hello" in message.text.lower() or "hi" in message.text.lower():
        bot.send_message(user_id, "Hello you!")
    else:
        bot.send_message(user_id, "Type \'Hello\' to begin")


bot.polling()
