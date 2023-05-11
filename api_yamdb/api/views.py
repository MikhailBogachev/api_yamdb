from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from reviews.models import Category, Review, Genre
from .serializers import CategorySerializer, CommentSerializer, GenreSerializer
from .permissions import AdminOrAuthorOrReadOnly, AdminOrReadOnly
from .mixins import GetPostDeleteViewSet


class CategoryViewSet(GetPostDeleteViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,  filters.SearchFilter)
    filterset_fields = ('name', 'slug')
    search_fields = ('name',)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        AdminOrAuthorOrReadOnly
    ]
    pagination_class = LimitOffsetPagination

    def get_review(self):
        return get_object_or_404(Review, pk=self.kwargs.get('review_id'))

    def get_queryset(self):
        return self.get_review().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.get_review())


class GenreViewSet(GetPostDeleteViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    filterset_fields = ('name', 'slug')
    search_fields = ('name',)
