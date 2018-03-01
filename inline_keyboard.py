import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import telegram


def make_keyboard(bot, update):
    chat_id = update.message.chat_id
    inline_buttons = [[InlineKeyboardButton(text='one', callback_data='1'),
                       InlineKeyboardButton(text='one', callback_data='2')],
                      [InlineKeyboardButton(text='three', callback_data='3')]]

    inline_keyboard = InlineKeyboardMarkup(inline_buttons)

    bot.send_message(
        chat_id=chat_id,
        text='Select one',
        reply_markup=inline_keyboard)


def inline_keyboard_callback(bot: telegram.bot.Bot, update: telegram.update.Update):
    query = update.callback_query
    chat_id = query.message.chat_id
    query_data = query.data
    message_id = query.message.message_id
    bot.edit_message_text(
        text=f'You choose {query_data}',
        chat_id=chat_id,
        message_id=message_id)


def main():
    updater = Updater(token='xxxx')
    dispacher = updater.dispatcher

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

    make_keyboard_handler = CommandHandler('inline', make_keyboard)
    inline_keyboard_handler = CallbackQueryHandler(inline_keyboard_callback)

    dispacher.add_handler(make_keyboard_handler)
    dispacher.add_handler(inline_keyboard_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
