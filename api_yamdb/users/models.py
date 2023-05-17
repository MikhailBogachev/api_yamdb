from django.contrib.auth.models import AbstractUser
from django.db import models


ROLE_CHOICES = [
    ("user", "Аутентифицированный пользователь"),
    ("moderator", "Модератор"),
    ("admin", "Администратор"),
]


class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    bio = models.TextField('Биография', blank=True)
    role = models.CharField('Роль', max_length=16,
                            choices=ROLE_CHOICES, default="user")
    confirmation_code = models.CharField(max_length=256, blank=True)
