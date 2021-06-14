from telegram import Update, ReplyKeyboardRemove
from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler,
    CallbackContext,
    MessageHandler,
    Filters)

from config import TG_TOKEN
from translator import go_trans
from keyboard import langBatton

CHOOSING, UA, EN = range(3)


def start(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        text="Цей бот вміє перекладати слова з Україньської на Російську та навпаки "
             "\n Для того щоб перекласти слово напишіть /translate",
        #
    )


def translate(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        text="Виберіть мовув для переклада",
        reply_markup=langBatton()
    )

    return CHOOSING


def ua_choose(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        text='Введіть слово',
        reply_markup=ReplyKeyboardRemove(),
    )

    return UA


def en_choose(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        text='Enter your word',
        reply_markup=ReplyKeyboardRemove(),
    )

    return EN


def do_eng_trans(update: Update, context: CallbackContext):
    text = update.effective_message.text
    update.effective_message.reply_text(
        text=go_trans(text, 'English')
    )

    return ConversationHandler.END


def do_ua_trans(update: Update, context: CallbackContext):
    text = update.effective_message.text
    update.effective_message.reply_text(
        text=go_trans(text, 'Ukrainian')
    )

    return ConversationHandler.END


def stop(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
        text='ну ок'
    )

    return ConversationHandler.END


def main():
    updater = Updater(token=TG_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('translate', translate)],
        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^English$'), en_choose
                ),
                MessageHandler(
                    Filters.regex('^Ukrainian$'), ua_choose
                ),
            ],
            UA: [
                MessageHandler(
                    Filters.text, do_ua_trans
                )
            ],
            EN: [
                MessageHandler(
                    Filters.text, do_eng_trans
                )
            ]
        },
        fallbacks=[MessageHandler(Filters.regex('Я передумала'), stop)],
    )

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
