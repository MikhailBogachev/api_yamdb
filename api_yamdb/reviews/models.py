from datetime import datetime
from django.core.validators import MaxValueValidator
from django.db import models


class Category(models.Model):
    """Категории (типы) произведений"""
    name = models.CharField(
        max_length=256,
        verbose_name='Название категории',
        help_text='Выбрать категорию')
    slug = models.SlugField(
        unique=True,
        max_length=50)
    description = models.TextField()


class Genre(models.Model):
    """Категории жанров"""
    name = models.CharField(
        max_length=256,
        verbose_name='Название жанра',
        help_text='Выбрать жанр')
    slug = models.SlugField(
        unique=True,
        max_length=50)
    description = models.TextField()
