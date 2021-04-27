from django.db import models

from django.conf import settings


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="date updated")

    def __str__(self):
        return self.title
