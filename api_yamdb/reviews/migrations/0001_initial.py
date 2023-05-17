# Generated by Django 3.2 on 2023-05-17 11:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import reviews.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Выбрать категорию', max_length=256, verbose_name='Категория')),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(message='Возможны только символы латинского алфавита,цифры и подчеркивание', regex='^[-a-zA-Z0-9_]+$')], verbose_name='Slug категории')),
            ],
            options={
                'verbose_name': 'Категория произведения',
                'verbose_name_plural': 'Категории произведения',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Выбрать жанр', max_length=256, verbose_name='Жанр')),
                ('slug', models.SlugField(unique=True, validators=[django.core.validators.RegexValidator(message='Возможны только символы латинского алфавита,цифры и подчеркивание', regex='^[-a-zA-Z0-9_]+$')], verbose_name='Slug жанра')),
            ],
            options={
                'verbose_name': 'Категория жанра',
                'verbose_name_plural': 'Категории жанров',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата публикации')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Указать название произведения', max_length=256, verbose_name='Название')),
                ('year', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(limit_value=reviews.validators.get_current_year, message='Произведение еще не вышло!')], verbose_name='Год выпуска')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.category', verbose_name='Slug категории')),
                ('genre', models.ManyToManyField(related_name='titles', to='reviews.Genre', verbose_name='Slug жанра')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
                'ordering': ['name'],
            },
        ),
    ]
