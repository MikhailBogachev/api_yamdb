from rest_framework import routers
from django.urls import path, include

from .views import (CategoryViewSet, CommentViewSet, TitleViewSet,
                    GenreViewSet, UserViewSet, APIUserMe)


app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'categories', CategoryViewSet, basename='categories')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(r'genres', GenreViewSet, basename='genres')
router_v1.register(r'users', UserViewSet, basename='users')
router_v1.register(r'titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/users/me/', APIUserMe.as_view(), name='user_me'),
    path('v1/', include(router_v1.urls)),
]
