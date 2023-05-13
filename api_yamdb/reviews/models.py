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


class Comment(models.Model):
    # """Комментарии к отзывам"""
    # review = models.ForeignKey(
    #     Rewiew,
    #     on_delete=models.CASCADE,
    #     related_name='comments'
    # )
    # author = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name='comments'
    # )
    # text = models.TextField()
    # pub_date = models.DateTimeField(
    #     'Дата добавления',
    #     auto_now_add=True,
    #     db_index=True
    # )

    # def __str__(self):
    #     return self.text
    pass


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
