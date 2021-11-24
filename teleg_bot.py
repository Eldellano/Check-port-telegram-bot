import telebot
import rotate

bot = telebot.TeleBot('2113531172:AAHQYikxVcodytj5l3vdLdQ8Lkp5T9HUqRc')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "check ports":
        bot.send_message(message.from_user.id, rotate.show_ports())
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
