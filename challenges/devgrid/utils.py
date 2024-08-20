import re
from datetime import datetime, timezone


def email_validator(email) -> bool:

    r = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

    valid = re.match(r, email)

    return not bool(valid)


def convert_datetime_utc():
    day = datetime.today().date().day
    month = datetime.today().date().month
    year = datetime.today().date().year
    dt = datetime(year, month, day)
    timestamp_utc = dt.replace(tzinfo=timezone.utc).timestamp()

    return timestamp_utc
