from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User

from album.models import Album
from album.api.serializers import AlbumSerializer


@api_view(['GET', ])
def api_detail_album_view(request, id):
    try:
        albums = Album.objects.get(id=id)
    except Album.DoesNotExist:
        return Response(satus=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlbumSerializer(albums)
        return Response(serializer.data)


@api_view(['PUT', ])
def api_update_album_view(request, id):
    try:
        albums = Album.objects.get(id=id)
    except Album.DoesNotExist:
        return Response(satus=status.HTTP_404_NOT_FOUND)

    albums = Album(owner=User.objects.get(pk=1))
    if request.method == 'PUT':
        serializer = AlbumSerializer(albums, data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update Successful"
            return Response(data=data)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_album_view(request, id):
    try:
        albums = Album.objects.get(id=id)
    except Album.DoesNotExist:
        return Response(satus=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = albums.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"

        return Response(data=data)


@api_view(['POST', ])
def api_create_album_view(request):
    account = User.objects.get(pk=1)

    album = Album(owner=account)

    if request.method == "POST":
        serializer = AlbumSerializer(album, data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

