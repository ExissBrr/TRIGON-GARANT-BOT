import functools


def format_phone(phone: str):
    if phone[0] == '8':
        phone = f'7{phone[1:]}'
    return str(functools.reduce(str.__add__, filter(str.isdigit, phone)))


def format_card_code(code: str):
    return str(functools.reduce(str.__add__, filter(str.isdigit, code)))
