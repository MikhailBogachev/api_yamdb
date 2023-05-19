from django.urls import path, include
from rest_framework import routers

from .views import (CategoryViewSet, CommentViewSet, TitleViewSet,
                    GenreViewSet, UserViewSet, APIUserRegister,
                    APIUserToken, ReviewViewSet)


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
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)


urlpatterns = [
    path('v1/auth/signup/', APIUserRegister.as_view(), name='user_register'),
    path('v1/auth/token/', APIUserToken.as_view(), name='user_token'),
    path('v1/', include(router_v1.urls)),
]
