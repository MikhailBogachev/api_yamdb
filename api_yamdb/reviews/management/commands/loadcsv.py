from csv import DictReader

from django.core.management import BaseCommand
from django.conf import settings

from reviews.models import Category, Genre, Title, Comment, Review
from users.models import User

path_csv = settings.STATICFILES_DIRS[1]
users_csv = path_csv / 'users.csv'
category_csv = path_csv / 'category.csv'
genre_csv = path_csv / 'genre.csv'
titles_csv = path_csv / 'titles.csv'
review_csv = path_csv / 'review.csv'
comments_csv = path_csv / 'comments.csv'


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for row in DictReader(
            open(category_csv, encoding='utf-8')
        ):
            category = Category(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )
            category.save()

        for row in DictReader(
            open(genre_csv, encoding='utf-8')
        ):
            category = Genre(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )
            category.save()

        for row in DictReader(
            open(users_csv, encoding='utf-8')
        ):
            category = User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name']
            )
            category.save()

        for row in DictReader(
            open(titles_csv, encoding='utf-8')
        ):
            title = Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category_id=row['category']
            )
            title.save()

        for row in DictReader(
            open(review_csv, encoding='utf-8')
        ):
            review = Review(
                id=row['id'],
                title_id=row['title_id'],
                text=row['text'],
                author_id=row['author'],
                score=row['score'],
                pub_date=row['pub_date']
            )
            review.save()

        for row in DictReader(
            open(comments_csv, encoding='utf-8')
        ):
            comment = Comment(
                id=row['id'],
                review_id=row['review_id'],
                text=row['text'],
                author_id=row['author'],
                pub_date=row['pub_date']
            )
            comment.save()
