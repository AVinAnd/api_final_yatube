from rest_framework import permissions


class AuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        """Для авторов или только чтение"""
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
