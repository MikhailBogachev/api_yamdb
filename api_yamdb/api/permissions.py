from django.contrib.auth import get_user_model
from rest_framework import permissions


User = get_user_model()


class AdminOrReadOnly(permissions.BasePermission):
    """
    Определяет права доступа:
    для SAFE_METHODS - все пользователи, включая анонимов.
    для остальных методов - только admin и superuser
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated
                and (request.user.is_admin
                     or request.user.is_superuser)
                )
        )


class AdminOrAuthorOrReadOnly(permissions.BasePermission):
    """
    Определяет права доступа:
    для SAFE_METHODS - все пользователи, включая анонимов.
    для POST - только аутентифицированные пользователи
    для остальных методов - admin, moderator и superuser
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated
                and (obj.author == request.user
                     or request.user.is_admin
                     or request.user.is_moderator
                     or request.user.is_superuser)
                )
        )


class IsAdmin(permissions.BasePermission):
    """
    Определяет права доступа:
    Только для пользователей, чья role = admin
    и суперюзеры
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (request.user.is_admin
                 or request.user.is_superuser)
        )
