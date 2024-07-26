import re
from datetime import datetime, timedelta
from math import floor


def age(born_date) -> int:
    today = datetime.now().date()
    age = today - born_date
    age = age.days/365
    return floor(age)


def email_validator(email) -> bool:

    r = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

    valid = re.match(r, email)

    return not bool(valid)


def cpf_validator(cpf) -> bool:
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return True

    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    if len(numbers) != 11 or len(set(numbers)) == 1:
        return True

    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return True

    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return True

    return False


def susep_validator(susep) -> bool:

    if not re.match(r'15414.6\d{5}/\d{4}-\d{2}', susep):
        return True


def buy_validate_age(min_age, age) -> bool:
    return True if min_age > age else False


def buy_validate_expired_date(expire_date, buy_date) -> bool:
    return True if buy_date > expire_date else False


def buy_validate_contribution(min_contribution, contribution) -> bool:
    return True if min_contribution > contribution else False


def rescue_min_days(min_days, plan_create_date):

    rescue_min_date = plan_create_date.date() + timedelta(days=min_days)
    now = datetime.now().date()

    return True if rescue_min_date > now else False


def value_rescue_validation(rescue_value, total_contrib):

    return True if rescue_value > total_contrib else False
