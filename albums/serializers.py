from albums.models import Album
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from photos.models import Photo
from photos.serializers import UploadPhotoSerializer


# class PhotoSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Photo
#         fields = ["title", "url", "album", "created_at", "updated_at"]
#

class AlbumSerializer(serializers.ModelSerializer):
    photos = UploadPhotoSerializer(many=True, read_only=True, default={})

    class Meta:
        model = Album
        fields = ["id", "title", "owner", "is_public", "photos", "created_at", "updated_at"]
