from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.keyboards.callback_data.message_distribution import distribution_cd, DistributionCommands


def make_keyboard(lang_code, messages):
    makrup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.inline.add_schedule,
                    callback_data=distribution_cd.new(id=0, command=DistributionCommands.ADD_SCHEDULE)
                )
            ]
        ]
    )
    if messages:
        for message in messages:
            makrup.add(
                InlineKeyboardButton(
                    text=f"{message.time} {message.text}",
                    callback_data=distribution_cd.new(id=message.id, command=DistributionCommands.SHOW_SCHEDULE)
                )
            )
    return makrup
