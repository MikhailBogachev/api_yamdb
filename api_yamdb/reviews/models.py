from django.db import models


class Category(models.Model):
    """Категории (типы) произведений"""
    name = models.CharField(
        max_length=256,
        verbose_name='Категория',
        help_text='Выбрать категорию'
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='Slug категории',
    )
    description = models.TextField()


class Genre(models.Model):
    """Категории жанров"""
    name = models.CharField(
        max_length=256,
        verbose_name='Жанр',
        help_text='Выбрать жанр')
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='Slug жанра'
    )
    description = models.TextField()
