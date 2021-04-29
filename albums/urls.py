from django.urls import path
from albums.views import CreateAlbumAPIView

app_name = 'albums'


urlpatterns = [
    path('albums/', CreateAlbumAPIView.as_view(), name="list")
]