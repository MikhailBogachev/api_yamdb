from django.db import models
from .validators import get_max_year_for_title, slug_validator
from users.models import User


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
        validators=[slug_validator],
        verbose_name='Slug категории'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория произведения'
        verbose_name_plural = 'Категории произведения'

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Комментарии к отзывам"""
    review = models.ForeignKey(
        Rewiew,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.text


class Genre(models.Model):
    """Категории жанров"""
    name = models.CharField(
        max_length=256,
        verbose_name='Жанр',
        help_text='Выбрать жанр'
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        validators=[slug_validator],
        verbose_name='Slug жанра'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория жанра'
        verbose_name_plural = 'Категории жанров'

    def __str__(self):
        return self.name


class Title(models.Model):
    """Произведения, к которым пишут отзывы
    (определённый фильм, книга или песенка)."""
    name = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Указать название произведения'
    )
    year = models.IntegerField(
        validators=[get_max_year_for_title],
        verbose_name='Год выпуска',
        null=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        null=True,
        verbose_name='Slug жанра',
        related_name='titles'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Slug категории',
        related_name='titles'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
