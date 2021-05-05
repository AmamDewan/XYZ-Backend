from rest_framework.permissions import BasePermission


class UserIsAlbumOwner(BasePermission):

    def has_permission(self, request, view):
        return False
