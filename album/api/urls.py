from django.urls import path
from album.api.views import (
    api_detail_album_view,
    api_update_album_view,
    api_delete_album_view,
    api_create_album_view
)


app_name = 'album'

urlpatterns = [
    path('<id>/', api_detail_album_view, name='detail'),
    path('<id>/update/', api_update_album_view, name='update'),
    path('<id>/delete/', api_delete_album_view, name='delete'),
    path('create/', api_create_album_view, name='create'),
]
