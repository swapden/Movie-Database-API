"""
Custom permissions
"""

from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Only admin / staff user will have all the permissions. Other users will have read only permissions.
    This is applied on Movie/Genre related views so that other users wont have create/update permissions.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to admin
        return request.user.is_superuser or request.user.is_staff


class IsAdminOrIsOwner(permissions.BasePermission):
    """
    Admin / staff users will have all the permissions
    Owner of object has all the permissions on his objects.
    """

    def has_object_permission(self, request, view, obj):
        # Permissions are only allowed to admin or owener
        return request.user.is_superuser or obj.username == request.user.username

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Admin wont have POST permission on views as this permission class will be used for Comment model.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return type(request.user) <> AnonymousUser and not request.user.is_superuser and not request.user.is_staff
        else:
            return type(request.user) <> AnonymousUser

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return (obj.owner == request.user)