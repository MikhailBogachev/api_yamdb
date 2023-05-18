from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLES_CHOICES = [
        (USER, 'Authenticated user'),
        (MODERATOR, 'Moderator'),
        (ADMIN, 'Administrator'),
    ]

    email = models.EmailField('Email', unique=True)
    bio = models.TextField('Биография', blank=True)
    role = models.CharField('Роль', max_length=16,
                            choices=ROLES_CHOICES, default=USER)
    confirmation_code = models.CharField(max_length=256, blank=True)

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR
