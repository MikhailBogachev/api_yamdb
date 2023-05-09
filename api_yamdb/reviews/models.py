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
