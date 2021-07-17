import datetime
import datetime as dt
from zoneinfo import ZoneInfo


def timezone(datetime: dt.datetime, timezone: int = 0, tz: ZoneInfo = datetime.timezone.utc) -> dt.datetime:
    return datetime.astimezone(tz) + dt.timedelta(hours=timezone)
