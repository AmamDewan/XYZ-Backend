from albums.models import Album
import json
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token


class CreateAlbumTestCase(APITestCase):
    url = reverse("albums:list")

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)

    def test_album_can_be_created(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.url, {"title": "album", "owner": self.user.id})
        self.assertEqual(201, response.status_code)

    def test_unauthenticated_user_cannot_create_album(self):
        response = self.client.post(self.url, {"title": "album", "owner": "1"})
        self.assertEqual(401, response.status_code)







