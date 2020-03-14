from datetime import datetime
from pytz import timezone


def convert_timezone(time: int, from_tz: timezone, to_tz: timezone) -> str:
    datetime_obj = datetime.fromtimestamp(time)
    datetime_obj_from = timezone(from_tz).localize(datetime_obj)
    datetime_obj_to = datetime_obj_from.astimezone(timezone(to_tz))
    return datetime_obj_to.strftime("%Y-%m-%d %I:%M:%S")

