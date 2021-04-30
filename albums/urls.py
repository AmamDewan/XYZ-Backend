from django.urls import path
from albums.views import CreateAlbumAPIView, DetailAlbumAPIView

app_name = 'albums'


urlpatterns = [
    path('albums/', CreateAlbumAPIView.as_view(), name="list"),
    path('albums/<int:pk>/', DetailAlbumAPIView.as_view(), name="detail")
]