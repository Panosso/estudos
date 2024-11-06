import re
import crud

from datetime import datetime, timezone, timedelta

def email_validator(email) -> bool:

    r = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

    valid = re.match(r, email)

    return bool(valid)

def convert_datetime_utc(today = datetime.today().date()):
    day = today.day
    month = today.month
    year = today.year
    dt = datetime(year, month, day)
    timestamp_utc = dt.replace(tzinfo=timezone.utc).timestamp()

    return timestamp_utc

def is_not_authorized(user):

    return False if user.is_loggin and user.date_to_log_active > (datetime.now()) else True