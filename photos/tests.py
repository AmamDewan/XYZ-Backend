from photos.models import Photo
from albums.models import Album
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class UploadPhotoTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('amam', 'amam@amam.me', 'super_password')
        self.album = Album.objects.create(title="Another Album", owner=self.user, is_public=True)
        self.token = Token.objects.create(user=self.user)
        self.url = reverse("albums:upload", kwargs={"pk": self.album.pk})
        self.file = open('./media/test/b1.PNG', 'rb')

    def test_photo_can_be_uploaded(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.url, {"title": "A title", "url": self.file, "album": self.album.pk}, )
        self.assertEqual(201, response.status_code)

    def test_only_owner_can_upload_photos_to_album(self):
        self.another_user = User.objects.create_user('harry', 'harry@potter.me', 'albus_serious_potter')
        self.client.force_login(self.another_user)
        response = self.client.post(self.url, {"title": "A title", "url": self.file, "album": self.album.pk}, )
        self.assertNotEqual(201, response.status_code)
        self.client.logout()

    # def test_image_url_acessable