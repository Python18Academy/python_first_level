
"""
Простой бот для отправки замедленные сообщения
This Bot uses the Updater class to handle the bot and the JobQueue для отправки замедленных сообщений.
Сначала определяется несколько обработчиков. Затем эти функции проходят через Dispatcher и получаются свое место в ответных сообщениях  
Потом, бот запускается, и не выключится пока не нажмете crl + C
Использование:
Простой бот будильник, который присылает сообщения после определеного промежутка времени
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging #часть библиотеки, которая отвечает за использование вашего бота


from telegram.ext import Updater, CommandHandler #Зачем CommandHandler нужен, думаю вопросов нет Updater позволяет отправлять сообщения

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Определяем наши основные команды.
def start(update, context):
    update.message.reply_text('Привет! Используй /set <seconds> чтобы установиться таймер')


def alarm(context):
    """Здесь устанавливаем значение нашего "Занятия", которое делает наш бот."""
    job = context.job
    context.bot.send_message(job.context, text='Бип-бип-бип')


def set_timer(update, context):
    """Добавляем занятие для нашего бота в очередь."""
    chat_id = update.message.chat_id
    try:
        # args[0] должен содержать количество времени 
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text('Мы не можем путешествовать во времени!((((')
            return

        # Добавляем наше дело в очередь и обнуляем сроки, если есть один такой
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(alarm, due, context=chat_id)
        context.chat_data['job'] = new_job

        update.message.reply_text('Таймер был успешн установлен!')

    except (IndexError, ValueError):
        update.message.reply_text('Использование: /set <seconds>')


def unset(update, context):
    """Нужно удалить занятие, если пользователь решил передумать"""
    if 'job' not in context.chat_data:
        update.message.reply_text('У вас нет активного таймера')
        return

    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']

    update.message.reply_text('Таймер был успешно удален')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Запускаем нашего бота"""
    # Создает экземпляр Update и передаем туда token нашего пользователя
    # Не забудьте установить use_context=True чтобы использовать 

    updater = Updater("1202446143:AAHFPF0fvtaRLToU40VSRIoDoWwdR-ikmZM", use_context=True)

    # получаем dispatcher, который поможет нам регистрировать наши соообщения
    dp = updater.dispatcher

    # прикрепляем наши функции к командам
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("set", set_timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))

    # Логируем все наши ошибки. Увидеть их можно будет только в консоли
    dp.add_error_handler(error)

    # Запускаем нашего бота
    updater.start_polling()

  #немного простой вариант start_polling()
    updater.idle()


if __name__ == '__main__':
    main()