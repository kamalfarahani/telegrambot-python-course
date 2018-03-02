import logging
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler


def make_keyboard(bot, update):
    custom_keyboard = [[KeyboardButton(text='hello')], 
                        [KeyboardButton(text='bye')]]
    
    kb_markup = ReplyKeyboardMarkup(custom_keyboard)

    bot.send_message(
        chat_id=update.message.chat_id,
        text='Making keyboard', 
        reply_markup=kb_markup)
    

def main():
    updater = Updater(token='TOKEN')
    dispacher = updater.dispatcher

    make_keyboard_handler = CommandHandler('keyboard', make_keyboard)
    dispacher.add_handler(make_keyboard_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
