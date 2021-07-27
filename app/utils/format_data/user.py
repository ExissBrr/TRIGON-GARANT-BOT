from typing import Union

from app.data.types.lang import LangCode
from app.utils.db_api.models.user import User


def format_username(username: Union[str, User], default: str = 'Not username') -> str:
    """
    Formatting username to string.
    Args:
        username: username

    Returns:
        Formatted username.
    """
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
