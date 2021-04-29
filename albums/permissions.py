from rest_framework.permissions import BasePermission


class UserIsAlbumOwner(BasePermission):

    def has_object_permission(self, request, view, album):
        return request.user.id == album.owner.id