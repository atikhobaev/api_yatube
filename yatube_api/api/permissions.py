from rest_framework.permissions import (
    BasePermission, SAFE_METHODS)


class IsAuthorOrReadOnly(BasePermission):
    """Определяет права на изменения только автора."""

    def has_permission(self, request, view):
        self.message = 'Для доступа к данной странице необходимо авторизоваться'
        if request.user.is_authenticated:
            return (
                request.method in SAFE_METHODS or 
                request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        self.message = 'Это действие доступно только владульцу данного поста'
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
