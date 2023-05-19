from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .validators import year_validator_for_title, slug_validator
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
        validators=[year_validator_for_title],
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


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    text = models.CharField(max_length=1024)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    score = models.IntegerField(
        validators=[
            MinValueValidator(1, 'Оценка должна быть не меньше 1!'),
            MaxValueValidator(10, 'Оценка должна быть не больше 10!')
        ],
        verbose_name='Оценка'
    )
    pub_date = models.DateTimeField(
        'дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique review'
            )
        ]
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-pub_date']

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Комментарии к отзывам"""
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
