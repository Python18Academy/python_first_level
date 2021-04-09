
# pip install pyTelegramBotAPI

import telebot
import re

token = '1706546567:AAEuglIh-gcmU8KnP3hebhjPUwkx5qUj3cg'

import random

devizions = ["Ozon Top", "Как же я люблю Ozon", "Всегда заказываю только на Ozon", 'Ozon лучшая компания на свете']

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def repeat_ozon_message(message):  # Название функции не играет никакой роли, в принципе
    if re.search(r'ozon', message.text):
        message.text = random.choice(devizions)
        bot.send_message(message.chat.id, message.text)


bot.infinity_polling()
