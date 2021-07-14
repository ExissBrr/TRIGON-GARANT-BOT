def antiflood_off(func):
    def wrapper(func):
        setattr(func, 'no_limit', True)
        return func
    return wrapper(func)
