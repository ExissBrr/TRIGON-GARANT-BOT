def make_start_link(bot_username: str, prefix: str, **url_params) -> str:
    """
    Create a link with transferred prefix and url params.

    Args:
        bot_username (str): Bot username.
        prefix (str): Prefix link.
        **url_params ():

    Returns:

    """
    data = f'{str(prefix).lower()}'

    for key, value in url_params.items():
        data += f'pp{str(key).lower()}oo{str(value).lower()}'

    if len(data) > 64:
        raise ValueError(f'Too big data({len(data)})! Maximum 64')

    return f'https://t.me/{bot_username}?start={data}'


def get_data_from_start_link(args: str) -> dict:
    """
    Returned data from args.
    Args:
        args (str): args from start link.

    Returns:
        prefix, args.
    """
    if args is None:
        return None

    data = {}

    args = args.split('pp')
    prefix = args.pop(0)

    if not prefix or prefix.find('=') != -1:
        return None

    data.setdefault('prefix', prefix.lower())
    for arg in args:
        key, value = map(str.lower, arg.split('oo'))
        if value == 'true':
            value = True
        elif value == 'false':
            value = False
        elif value == '' or value == 'none':
            value = None
        data.setdefault(key, value)

    return data
