from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.data.types.user_data import UserRole
from app.keyboards.callback_data.user import user_cd, UserCommand
from app.utils.db_api.models.user import User


async def make_keyboard_user_interaction(lang_code, found_user_id, user_id):
    markup = InlineKeyboardMarkup()
    if found_user_id != user_id:
        markup.row(
            InlineKeyboardButton(
                text=text[lang_code].button.inline.create_deal,
                callback_data=user_cd.new(user_id=found_user_id,
                                          command=UserCommand.CREATE_DEAL)
            ),
        )
    markup.insert(
        InlineKeyboardButton(
            text=text[lang_code].button.inline.show_feedbacks,
            callback_data=user_cd.new(user_id=found_user_id, command=UserCommand.GET_SELLER_FEEDBACKS)
        )
    )
    user: User = await User.get(int(user_id))
    if user.role == UserRole.ADMIN:
        markup.row(
            InlineKeyboardButton(
                text=text[lang_code].button.inline.more_info,
                callback_data=user_cd.new(user_id=found_user_id, command=UserCommand.SHOW_MORE_INFO)
            )
        )
    return markup
