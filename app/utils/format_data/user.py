from typing import Union

from app.data.types.bargain_data import DealRate
from app.data.types.lang import LangCode
from app.utils.db_api.models.user import User


def format_username(username: Union[str, User], default: str = 'Not username') -> str:
    """Форматирует username"""
    if isinstance(username, User):
        username = username.username

    if str(username) == 'None':
        username = default
    else:
        username = '@' + username

    return username


def format_fullname(fullname: Union[str, User]) -> str:
    """
    Formatting user fullname.
    Replace html symbol to html code.
    Args:
        fullname: String.

    Returns:
        Formatted user fullname.

    """
    if isinstance(fullname, User):
        fullname = fullname.fullname

    fullname = fullname.replace('<', '&lt;')
    fullname = fullname.replace('>', '&gt;')
    fullname = fullname.replace(' ', '👻')

    return fullname


def format_lang_code(lang_code: str) -> str:
    """
    Formatting language code to string.
    Args:
        lang_code: language code.

    Returns:
        String formatted language code.

    """
    if lang_code == LangCode.RU:
        return '🇷🇺 Русский'
    elif lang_code == LangCode.ENG:
        return '🇺🇸 English'

    return 'He yдaлocb oпpeдeлutb Я3ыk'


def format_rate(total: float, count):
    if total == DealRate.NONE or total is None or count == 0:
        return '-'
    total /= count
    rate_star = "🌕" * int(total)
    if total % 1 >= 0.7:
        rate_star += "🌖"
    elif total % 1 >= 0.5:
        rate_star += '🌗'
    elif total % 1 >= 0.2:
        rate_star += '🌘'
    dark_star = int(5 - total) * "🌑"
    rate_star += dark_star
    return rate_star
