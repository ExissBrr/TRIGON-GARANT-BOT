from app.utils.format_data.requisite import format_card_code, format_phone


def is_valid_card(code: str):
    code = format_card_code(code)
    LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    evens = sum(int(i) for i in code[-1::-2])
    odds = sum(LOOKUP[int(i)] for i in code[-2::-2])
    return ((evens + odds) % 10 == 0)


def is_valid_phone(phone: str):
    phone = format_phone(phone)
    return len(phone) == 11


def is_valid_details(detail: str):
    detail = detail.replace(' ', '')
    if len(detail) == 16 and is_valid_card(detail):
        return True
    if '+7' in detail or '+38' in detail:
        return True

    return False
