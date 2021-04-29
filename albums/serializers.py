from albums.models import Album
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class CreateAlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ("id", "title", "owner", "is_public", "created_at")


