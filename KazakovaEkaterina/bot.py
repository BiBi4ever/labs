import telebot
from telebot import types
bot = telebot.TeleBot('1667962581:AAFL4auEJZPrQjq5fXNMdFPSVZUeN7_J5p8')
@bot.message_handler(commands=['start','go'])
def message_help(message):
    # Создаем кнопку
    startmenu = types.ReplyKeyboardMarkup(True, True)
    startmenu.row('Нажимай! 😇')
    # Отправляем сообщение и отправляем подключение клавиатуры
    bot.send_message(message.chat.id,'Добро пожаловать!✋ \nЯ бесплатный бот-помощник!', reply_markup=startmenu)
@bot.message_handler(content_types=['text'])
def send_smth(message):
    if "привет" in message.text.lower() or "hello" in message.text.lower() or "здравствуй" in message.text.lower() or "hi" in message.text.lower():
        bot.send_message(message.chat.id, 'Приветсвую тебя в лучшем бот-помощнике для лаборотории!')
    else:
        bot.send_message(message.chat.id, "Поприветствуй меня!😇")


bot.polling()
