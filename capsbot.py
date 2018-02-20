from telegram.ext import Updater, CommandHandler


def caps(bot, update, args):
    print(args)
    text_caps = ' '.join(args).upper()
    update.message.reply_text(text_caps)


def main():
    updater = Updater(token='TOKEN')
    dispacher = updater.dispatcher

    caps_handler = CommandHandler('caps', caps, pass_args=True)
    dispacher.add_handler(caps_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
