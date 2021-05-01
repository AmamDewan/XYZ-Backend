from photos.models import Photo
from rest_framework import serializers
# from albums.serializers import AlbumSerializer

class UploadPhotoSerializer(serializers.ModelSerializer):
    # album = AlbumSerializer(read_only=True)
    class Meta:
        model = Photo
        fields = ["title", "url", "album", "created_at", "updated_at"]

