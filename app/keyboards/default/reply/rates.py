from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def keyboard_choose_rate():
    markup = ReplyKeyboardMarkup()
    for i in range(1, 6):
        markup.add(
            KeyboardButton(
                text=str(i)
            )
        )
    return markup
