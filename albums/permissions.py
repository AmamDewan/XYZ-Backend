from rest_framework.permissions import BasePermission


class UserIsAlbumOwner(BasePermission):

    def has_object_permission(self, request, view, album):
        return request.user.id == album.owner.id

    # def has_permission(self, request, view):
    #     return self.has_object_permission(request, view)

class IsAlbumPublic(BasePermission):

    def has_object_permission(self, request, view, album):
        return album.is_public
