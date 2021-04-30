from rest_framework.permissions import BasePermission


class UserIsAlbumOwner(BasePermission):

    def has_object_permission(self, request, view, album):
        return request.user.id == album.owner.id


class IsAlbumPublic(BasePermission):

    def has_object_permission(self, request, view, album):
        return album.is_public
