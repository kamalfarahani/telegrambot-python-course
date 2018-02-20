from telegram.ext import Updater
from telegram.ext import CommandHandler


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id, text="Hey I'm a bot")

    #update.message.reply_text("Hey I'm a bot")



def main():
    updater = Updater(token='TOKEN')
    dispacher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispacher.add_handler(start_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
