from telegram.ext import Updater, CommandHandler


def send_photo(bot, update):
    bot.send_photo(
        chat_id=update.message.chat_id, photo=open('./Tree.jpg', 'rb'))


def main():
    updater = Updater(token='TOKEN')
    dispacher = updater.dispatcher

    send_photo_handler = CommandHandler('image', send_photo)
    dispacher.add_handler(send_photo_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
