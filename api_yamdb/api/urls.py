from rest_framework import routers
from django.urls import path, include
from .views import CategoryViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'categories', CategoryViewSet, basename='categories')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]