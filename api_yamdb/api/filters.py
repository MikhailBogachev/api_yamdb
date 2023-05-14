from django_filters.rest_framework import FilterSet, CharFilter
from reviews.models import Title


class TitleFilter(FilterSet):
    category = CharFilter(field_name='category__slug')
    genre = CharFilter(field_name='genre__slug')
    name = CharFilter(field_name='title__name')
    year = CharFilter(field_name='title__year')

    class Meta:
        model = Title
        fields = ['category', 'genre', 'name', 'year']
