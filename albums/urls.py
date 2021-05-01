from django.urls import path
from albums.views import CreateAlbumAPIView, DetailAlbumAPIView
from photos.views import UploadPhotoAPIView

app_name = 'albums'


urlpatterns = [
    path('albums/', CreateAlbumAPIView.as_view(), name="list"),
    path('albums/<int:pk>/', DetailAlbumAPIView.as_view(), name="detail"),
    path('albums/<int:pk>/photos/', UploadPhotoAPIView.as_view(), name="upload")
]
