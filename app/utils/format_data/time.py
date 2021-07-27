import datetime


def timezone(dt: datetime.datetime, gmt: int = 0) -> datetime.datetime:
    return dt + datetime.timedelta(hours=gmt)
