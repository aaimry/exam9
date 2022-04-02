from django.urls import path

from .views import (IndexView,
                    CreatePhotoView,
                    PhotoUpdateView,
                    PhotoView,
                    PhotoDeleteView,
                    AlbumView,
                    CreateAlbumView,
                    AlbumUpdateView,
                    AlbumDeleteView,
                    GetPhotoByLink,
                    GenerateLink)

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index_photo'),
    path('photos/<int:pk>', PhotoView.as_view(), name='view_photo'),
    path('photos/add', CreatePhotoView.as_view(), name='create_photo'),
    path('photos/delete/<int:pk>/', PhotoDeleteView.as_view(), name='delete_photo'),
    path('photos/update/<int:pk>/', PhotoUpdateView.as_view(), name='update_photo'),
    path('album/<int:pk>', AlbumView.as_view(), name='view_album'),
    path('album/add', CreateAlbumView.as_view(), name='create_album'),
    path('album/update/<int:pk>/', AlbumUpdateView.as_view(), name='update_album'),
    path('album/delete/<int:pk>/', AlbumDeleteView.as_view(), name='delete_album'),
    path('<int:pk>/get_uuid', GenerateLink.as_view(), name='generate_link'),
    path('token/<uuid>', GetPhotoByLink.as_view(), name='get_photo_by_link'),
]
