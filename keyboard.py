from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

BUTTON1_ENG = "English"
BUTTON2_UA = "Ukrainian"


def langBatton():
    keyboard = [
        [
            KeyboardButton(BUTTON2_UA),
            KeyboardButton(BUTTON1_ENG),
        ],
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
