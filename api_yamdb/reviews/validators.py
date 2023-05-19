from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


def year_validator_for_title(value):
    if value > timezone.now().year:
        raise ValidationError(
            'Проверьте год. Произведение еще не вышло!'
        )


slug_validator = RegexValidator(
    regex='^[-a-zA-Z0-9_]+$',
    message=(
        R'Возможны только символы латинского алфавита,'
        R'цифры и подчеркивание'
    )
)
