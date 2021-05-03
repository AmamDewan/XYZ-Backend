from django.db import models
from albums.models import Album


# Create your models here.
def to_name(instance):
    return str(instance).replace(' ', '-').lower()

def get_location(instance, filename):
    return '/'.join(['users', to_name(instance.album.owner), to_name(instance.album), filename])


class Photo(models.Model):
    title = models.CharField(max_length=50, blank=True)
    url = models.ImageField(upload_to=get_location, null=False, blank=False)
    # exif will be added here
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=False, related_name='photos')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="date updated")

    def __str__(self):
        return self.title

