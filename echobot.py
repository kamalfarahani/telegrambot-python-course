from telegram.ext import Updater, MessageHandler, Filters


def echo(bot, update):
    msg = 'Echo: ' + update.message.text
    update.message.reply_text(msg)


def main():
    updater = Updater(token='TOKEN')
    dispacher = updater.dispatcher

    echo_handler = MessageHandler(Filters.text, echo)
    dispacher.add_handler(echo_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
