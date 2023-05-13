from datetime import datetime

from django.core.validators import RegexValidator, MaxValueValidator


def get_current_year():
    return datetime.now().year


def get_max_year_for_title():
    return MaxValueValidator(
        limit_value=get_current_year,
        message='Произведение еще не вышло!'
    )


def slug_validator():
    return RegexValidator(
        regex='^[-a-zA-Z0-9_]+$',
        message=(
            R'Возможны только символы латинского алфавита,'
            R'цифры и подчеркивание'
        )
    )
