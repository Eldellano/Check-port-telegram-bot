from telebot import *
import rotate

bot = telebot.TeleBot('2113531172:AAHQYikxVcodytj5l3vdLdQ8Lkp5T9HUqRc')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

markup = types.ReplyKeyboardMarkup()
itembtn = types.KeyboardButton('check ports')
markup.row(itembtn)
# tb.send_message(chat_id, "Choose one letter:", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "check ports":
        for i in rotate.run_rotate():
            bot.send_message(message.from_user.id, i)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши  /help.")


bot.polling(none_stop=True, interval=0)
