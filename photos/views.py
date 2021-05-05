from rest_framework.generics import CreateAPIView
from photos.serializers import UploadPhotoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from photos.permissions import UserIsAlbumOwner
from albums.models import Album

class UploadPhotoAPIView(CreateAPIView):
    serializer_class = UploadPhotoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        album = Album.objects.get(pk=request.data["album"])
        if album.owner.pk == int(request.data["album"]):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            data = serializer.data

            headers = self.get_success_headers(serializer.data)
            return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        return Response('You are not allowed to post another user album', status=status.HTTP_401_UNAUTHORIZED)
    # def perform_create(self, serializer):



