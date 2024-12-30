from django.core.exceptions import ValidationError
import re

def strong_password(password):
    regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])')

    if not regex.match(password):
        raise ValidationError({
            "Passwd fraco"
        },
        code='Invalid'
        )