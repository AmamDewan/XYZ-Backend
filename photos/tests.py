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

    def test_photo_can_be_uploaded(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.file = open('./media/test/b1.PNG', 'rb')
        response = self.client.post(self.url, {"url": self.file, "album": self.album.pk}, )
        self.assertEqual(201, response.status_code)



