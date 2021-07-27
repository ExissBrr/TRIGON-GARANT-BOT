import random
import string
from typing import Union


def generate_random_text(length: int = 6, ascii_uppercase: bool = True, digits: bool = True):
    chars = ''
    if ascii_uppercase:
        chars += string.ascii_uppercase
    if digits:
        chars += string.digits

    return ''.join([random.choice(chars) for i in range(length)])

def shuffle_text(text: Union[list[str], str]):
    if isinstance(text, list) and text:
        text = random.choice(text)

    _text = list(str(text).upper())
    random.shuffle(_text)
    return ''.join(_text)
