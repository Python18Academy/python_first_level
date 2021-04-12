"""
простой бот, цель которого - получать информацию о фильмах студии Гимли
https://ghibliapi.herokuapp.com/#tag/Films

вам потребуются следующие импорты
pip install python-telegram-bot --upgrade
token = '1706546567:AAEuglIh-gcmU8KnP3hebhjPUwkx5qUj3cg'
logging встроенная библиотека для логирования событий

pip install pyTelegramBotAPI
"""


import requests
import logging
from telegram.ext import Updater, CommandHandler



# Определяем наши основные команды.
def start(update, context):
    update.message.reply_text('Привет! Используй /get <film> чтобы получить информацию о фильме')


def send_data(context, info):
    """Здесь устанавливаем значение нашего "Занятия", которое делает наш бот."""
    job = context
    context.bot.send_message(job, text=info)


def get_info(update, context):
    """Добавляем занятие для нашего бота в очередь."""
    chat_id = update.message.chat_id
    # try:
        # args[0] должен содержать количество времени
    due = context.args[0]

        # Добавляем наше дело в очередь и обнуляем сроки, если есть один такой
    # if 'job' in context.chat_data:
    #         old_job = context.chat_data['job']
    #         old_job.schedule_removal()
    #     new_job = context.job_queue.run_once(send_data(), due, context=chat_id)
    #     context.chat_data['job'] = new_job
    context.job_queue.run_once(send_data(chat_id,due), due, context=chat_id)
    update.message.reply_text(due) # здесь отвечаем фильмом, но для этого нам нужно  распарсить json

    # except (IndexError, ValueError):
    #     update.message.reply_text('Использование: /get <film>')

def main():
    """Запускаем нашего бота"""
    # Создает экземпляр Update и передаем туда token нашего пользователя
    # Не забудьте установить use_context=True чтобы использовать

    updater = Updater("1706546567:AAEuglIh-gcmU8KnP3hebhjPUwkx5qUj3cg", use_context=True)

    # получаем dispatcher, который поможет нам регистрировать наши соообщения
    dp = updater.dispatcher

    # прикрепляем наши функции к командам
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("get", get_info,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))

    # Логируем все наши ошибки. Увидеть их можно будет только в консоли


    # Запускаем нашего бота
    updater.start_polling()

  #немного простой вариант start_polling()
    updater.idle()


if __name__ == '__main__':
    main()