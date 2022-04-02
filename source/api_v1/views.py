from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, JsonResponse
from django.views import View
from rest_framework.generics import get_object_or_404

from webapp.models import Photo, PhotoFav, Album, AlbumFav


class FavView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        photo = get_object_or_404(Photo, id=kwargs.get('pk'))
        user_fav = user.photo_fav.all()
        if user_fav.filter(photo=photo).count() > 0:
            return HttpResponseForbidden('Вы уже постаивли лайк :)')
        else:
            PhotoFav.objects.create(user=user, photo=photo).save()
        return JsonResponse({'id': photo.pk})


class UnFavView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        photo = get_object_or_404(Photo, id=kwargs.get('pk'))
        user_fav = user.photo_fav.all()
        if user_fav.filter(photo=photo).count() > 0:
            PhotoFav.objects.get(user=user, photo=photo).delete()
        else:
            return HttpResponseForbidden('Кажется, вашего лайка тут и не было :(')
        return JsonResponse({'id': photo.pk})


class AlbumFavView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        album = get_object_or_404(Album, id=kwargs.get('pk'))
        user_fav = user.album_fav.all()
        if user_fav.filter(album=album).count() > 0:
            return HttpResponseForbidden('Вы уже постаивли лайк :)')
        else:
            AlbumFav.objects.create(user=user, album=album).save()
        return JsonResponse({'id': album.pk})


class AlbumUnFavView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        album = get_object_or_404(Album, id=kwargs.get('pk'))
        user_fav = user.album_fav.all()
        if user_fav.filter(album=album).count() > 0:
            AlbumFav.objects.get(user=user, album=album).delete()
        else:
            return HttpResponseForbidden('Кажется, вашего лайка тут и не было :(')
        return JsonResponse({'id': album.pk})
