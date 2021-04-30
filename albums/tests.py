from albums.models import Album
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class CreateAlbumTestCase(APITestCase):
    url = reverse("albums:list")

    def setUp(self):
        self.username = "amam"
        self.email = "amam@amam.com"
        self.password = "super_password"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)

    def test_album_can_be_created(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.url, {"title": "album", "owner": self.user.pk})
        self.assertEqual(201, response.status_code)

    def test_unauthenticated_user_cannot_create_album(self):
        response = self.client.post(self.url, {"title": "album", "owner": self.user.pk})
        self.assertEqual(401, response.status_code)


class FetchAlbumTestCase(APITestCase):
    url = reverse("albums:list")

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.album = Album.objects.create(title="Album title", owner=self.user, is_public=True)
        self.token = Token.objects.create(user=self.user)
        self.albumUrl = reverse("albums:detail", kwargs={"pk": self.album.pk})

    def test_albums_can_be_fetched(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_public_album_can_be_fetched_by_url(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(self.albumUrl)
        self.assertEqual(200, response.status_code)

    def test_only_owner_can_see_private_album_by_url(self):
        another_user = User.objects.create_user('ex user', 'ex@ex.com', 'aPassword')
        another_album = Album.objects.create(title="Album title", owner=another_user, is_public=False)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        # self.client.force_authenticate(user=another_user)
        response = self.client.get(reverse("albums:detail", kwargs={"pk": another_album.pk}))
        self.assertNotEqual(200, response.status_code)
