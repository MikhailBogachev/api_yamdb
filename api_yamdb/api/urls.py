from rest_framework import routers
from django.urls import path, include
from .views import CategoryViewSet, CommentViewSet, GenreViewSet


app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'categories', CategoryViewSet, basename='categories')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(r'genres', GenreViewSet, basename='genres')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
