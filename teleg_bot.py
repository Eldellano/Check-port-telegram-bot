from telebot import *
import rotate
import time
import re
import port_data

token = ''  # pun your bot token!
bot = telebot.TeleBot(token)

# buttons for quickly send request
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
itembtn_1 = types.KeyboardButton('check ports')
itembtn_2 = types.KeyboardButton('extra')
markup.row(itembtn_1, itembtn_2)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Бот позволяет отслеживать статус твоих сетевых портов. '
                          'Порты для отслеживания можно добавить и удалить.')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'check ports':
        for i in rotate.run_rotate():
            bot.send_message(message.from_user.id, i, reply_markup=markup)
    elif message.text == 'extra':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Add port', 'Del port', 'Back']
        keyboard.row(*buttons)
        bot.send_message(message.from_user.id, 'Выбери пункт', reply_markup=keyboard)
    elif message.text == 'Add port':
        keyboard = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.from_user.id, 'Введи порт и имя сервиса через пробел', reply_markup=keyboard)
    elif message.text == 'Del port':
        keyboard = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.from_user.id, 'Введи порт', reply_markup=keyboard)
    elif message.text == 'Back':
        bot.send_message(message.from_user.id, 'Выбери пункт', reply_markup=markup)
    # add new port
    elif re.search(r'([0-9]+)(.)(\D+)', message.text):
        match = re.search(r'([0-9]+)(.)(.+)', message.text)
        port_data.DataBase().port_add(match.group(1), match.group(3))
        bot.send_message(message.from_user.id, 'Порт ' + match.group(1) + ' добавлен', reply_markup=markup)
    # delete port
    elif re.search(r'([0-9]+)', message.text):
        match = re.search(r'([0-9]+)', message.text)
        port_data.DataBase().port_del(match.group(1))
        bot.send_message(message.from_user.id, 'Порт ' + match.group() + ' удален', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши  /help.')


# run bot, waiting reconnect if no internet
while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=30)
    except:  # TODO: add catch ConnectionError
        time.sleep(6)
# bot.polling(none_stop=True, interval=0, timeout=30)
