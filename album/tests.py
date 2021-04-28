from django.test import TestCase
from album.models import Album
from django.contrib.auth.models import User


# Create your tests here.
class AlbumTasteCase(TestCase):
    # def setUp(self):
    #     newUser = User.objects.create(username='abcd', email='amam@aamam.me')
    #     # Album.objects.create(title='xyz')



    def test_album_must_have_owner(self):
        newUser = User.objects.create(username='abcd', email='amam@aamam.me')
        Album.objects.create(title='xyz', owner=newUser)
        res = Album.objects.get(title='xyz')
        self.assertEqual(res.owner, newUser)


    # def test_user_can_see_album(self):
    #
    #     res = Album.objects.get(title='xyz')
    #
    #     self.assertNotEqual()