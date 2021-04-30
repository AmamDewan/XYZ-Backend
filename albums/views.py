from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from albums.serializers import AlbumSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from albums.models import Album
from albums.permissions import IsAlbumPublic, UserIsAlbumOwner


class CreateAlbumAPIView(ListCreateAPIView):
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data = serializer.data

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class DetailAlbumAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    permission_classes = [IsAlbumPublic | UserIsAlbumOwner]

    queryset = Album.objects.all()
