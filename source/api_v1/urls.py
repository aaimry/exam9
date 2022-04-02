from django.urls import path

from api_v1.views import FavView, UnFavView, AlbumFavView, AlbumUnFavView

app_name = 'api'
urlpatterns = [
    path('photo_fav/<int:pk>', FavView.as_view(), name='photo_fav'),
    path('photo_unfav/<int:pk>', UnFavView.as_view(), name='photo_unfav'),
    path('album_fav/<int:pk>', AlbumFavView.as_view(), name='album_fav'),
    path('album_unfav/<int:pk>', AlbumUnFavView.as_view(), name='album_unfav')
]
