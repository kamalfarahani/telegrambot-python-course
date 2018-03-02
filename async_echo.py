from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext.dispatcher import run_async
import threading
import time

@run_async
def echo(bot, update):
    print(threading.get_ident())
    time.sleep(5)
    
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
