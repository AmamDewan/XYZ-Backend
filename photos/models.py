from django.db import models
from albums.models import Album


# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    url = models.CharField(max_length=200, null=False, blank=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="date updated")

    def __str__(self):
        return self.title
