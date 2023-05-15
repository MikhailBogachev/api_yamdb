from datetime import datetime

from django.core.validators import RegexValidator, MaxValueValidator


def get_current_year():
    return datetime.now().year


get_max_year_for_title = MaxValueValidator(
        limit_value=get_current_year,
        message='Произведение еще не вышло!'
    )


slug_validator = RegexValidator(
        regex='^[-a-zA-Z0-9_]+$',
        message=(
            R'Возможны только символы латинского алфавита,'
            R'цифры и подчеркивание'
        )
    )
