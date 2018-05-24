import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Как будем логинится
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Передает сообщение когда вызван старт
def start(update, context):
    update.message.reply_text('Hello it is view_2_bot!')


def help(update, context):
    update.message.reply_text('Help is now unavailable ...')


#   Печчатаем сообщение пользователя
def echo(update, context):
   update.message.reply_text(update.message.text)


# Логи ошибок во время update
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    updater = Updater("597555709:AAG6cIe9Ncq5GlNHmPLadx7YhPrtYTX8Cz0")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()     #   запускаем

    # работаем пока не Ctrc-C
    updater.idle()


if __name__ == '__main__':
    main()