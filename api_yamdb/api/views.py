from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets, permissions, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import (LimitOffsetPagination,
                                       PageNumberPagination)

from reviews.models import Category, Genre, Title, Review
from .permissions import AdminOrAuthorOrReadOnly, AdminOrReadOnly, IsAdmin
from .mixins import GetPostDeleteViewSet
from .filters import TitleFilter
from .serializers import (
    CategorySerializer, CommentSerializer, GenreSerializer, TitleReciveSerializer, TitleCreateSetrializer,
    ReviewSerializer, UserSerializer, UserRegisterSerializer, 
    UserTokenSrializer, UserMeSerializer
)


User = get_user_model()


class CategoryViewSet(GetPostDeleteViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('name', 'slug')
    search_fields = ('name',)
    lookup_field = 'slug'


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AdminOrAuthorOrReadOnly]
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
    filter_backends = (DjangoFilterBackend,  filters.SearchFilter)
    filterset_fields = ('name', 'slug')
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleReciveSerializer
    permission_classes = [AdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,  filters.SearchFilter)
    filterset_class = TitleFilter
    search_fields = ('name',)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TitleReciveSerializer
        return TitleCreateSetrializer

      
class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [AdminOrAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination
    
    def get_title(self):
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self.get_title().reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    # Исключаем метод PUT
    http_method_names = ["get", "post", "patch", "delete"]

    def retrieve(self, request, *args, **kwargs):
        username = kwargs.get('pk', None)
        user = get_object_or_404(User, username=username)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        username = kwargs.get('pk', None)
        user = get_object_or_404(User, username=username)
        serializer = self.get_serializer(user, data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        username = kwargs.get('pk', None)
        user = get_object_or_404(User, username=username)
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class APIUserMe(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):
        user = User.objects.get(username=request.user)
        serializer = UserMeSerializer(user)
        return Response(serializer.data)

    def patch(self, request):
        user = get_object_or_404(User, username=request.user)
        serializer = UserMeSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIUserRegister(APIView):
    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        user, _ = User.objects.get_or_create(**serializer.validated_data)
        confirmation_code = default_token_generator.make_token(user)
        user.confirmation_code = confirmation_code
        user.save()

        send_mail(
            "Confirmation code apiyamdb",
            f"Your confirmation code: {confirmation_code}",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class APIUserToken(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserTokenSrializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        confirmation_code = serializer.validated_data.get('confirmation_code')
        username = serializer.validated_data.get('username')
        user = get_object_or_404(User, username=username)
        print(user.confirmation_code)
        if user.confirmation_code != confirmation_code:
            return Response({'message': 'Invalid confirmation_code'},
                            status=status.HTTP_400_BAD_REQUEST)
        refresh = RefreshToken.for_user(user)
        return Response({'token': str(refresh.access_token)})
