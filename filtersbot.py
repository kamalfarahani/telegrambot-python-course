from telegram.ext import Updater, MessageHandler, Filters, BaseFilter


class HelloFilter(BaseFilter):

    def filter(self, message):
        return 'hello' in message.text.lower()


def photo_or_video(bot, update):
    update.message.reply_text('This is photo or video')


def forwarded_text(bot, update):
    update.message.reply_text('This is a forwarded text')


def not_forwarded_text(bot, update):
    update.message.reply_text('This is just a text')


def hello(bot, update):
    update.message.reply_text('Hello back')


def main():
    updater = Updater(token='TOKEN')
    dispacher = updater.dispatcher

    photo_or_video_handler = MessageHandler(
        Filters.photo | Filters.video, photo_or_video)

    forwarded_text_handler = MessageHandler(
        Filters.text & Filters.forwarded, forwarded_text)

    not_forwarded_text_handler = MessageHandler(
        Filters.text & ~Filters.forwarded, not_forwarded_text)

    hello_filter = HelloFilter()
    hello_handler = MessageHandler(hello_filter, hello)

    dispacher.add_handler(photo_or_video_handler)
    dispacher.add_handler(forwarded_text_handler)
    # Change order of next two lines and see result
    dispacher.add_handler(hello_handler)
    dispacher.add_handler(not_forwarded_text_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
