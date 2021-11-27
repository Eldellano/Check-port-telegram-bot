from telebot import *
import rotate
import time

bot = telebot.TeleBot('2113531172:AAHQYikxVcodytj5l3vdLdQ8Lkp5T9HUqRc')

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")

# buttons for quickly send request
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
itembtn_1 = types.KeyboardButton('check ports')
itembtn_2 = types.KeyboardButton('help')
markup.row(itembtn_1, itembtn_2)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "check ports":
        for i in rotate.run_rotate():
            bot.send_message(message.from_user.id, i, reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши  /help.")


# run bot, waiting reconnect if no internet
while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=30)
    except:
        time.sleep(5)
