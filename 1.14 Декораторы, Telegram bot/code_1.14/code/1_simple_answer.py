

# pip install pyTelegramBotAPI

import telebot # telebot для начала
token = '1706546567:AAEuglIh-gcmU8KnP3hebhjPUwkx5qUj3cg'


bot = telebot.TeleBot(token) # создаем бота

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()

