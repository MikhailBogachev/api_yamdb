from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination
from reviews.models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = LimitOffsetPagination
