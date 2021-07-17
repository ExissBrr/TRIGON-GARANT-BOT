import datetime
import datetime as dt
from zoneinfo import ZoneInfo


def timezone(datetime: dt.datetime, timezone: int = 0) -> dt.datetime:
    return datetime + dt.timedelta(hours=timezone)
