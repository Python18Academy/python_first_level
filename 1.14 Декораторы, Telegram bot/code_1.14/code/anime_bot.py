import telebot # telebot для начала
import requests
import json
import re
token = '1706546567:AAEuglIh-gcmU8KnP3hebhjPUwkx5qUj3cg'


bot = telebot.TeleBot(token) # создаем бота

@bot.message_handler(commands=['start'])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    data = "Привет! Не знаешь какое аниме посмотреть? Спроси меня /anime <title_anime> "
    bot.send_message(message.chat.id, data)

@bot.message_handler(commands=['anime'])
def get_anime(message):
    if re.search(r'\s[a-z]+', message.text):
      title = re.search(r'\s[a-z\s]+', message.text)
      title = title.group(0)
      data = requests.get(f'https://api.jikan.moe/v3/search/anime?q={title}')
      data = data.text
      info = json.loads(data)
      bot.send_photo(message.chat.id, info['results'][0]['image_url'])
      bot.send_message(message.chat.id, info['results'][0]['url'])
    else:
      bot.send_message(message.chat.id, "что то тут не так")


bot.infinity_polling()