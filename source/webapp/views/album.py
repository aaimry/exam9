from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse, reverse_lazy

from webapp.models import Photo, Album
from webapp.forms import AlbumForm


class AlbumView(DetailView):
    model = Album
    template_name = 'album/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Gallery.objects.filter(album=self.object).exclude(is_private=True)
        context['is_author'] = self.object.author == self.request.user
        return context


class CreateAlbumView(LoginRequiredMixin, CreateView):
    template_name = 'album/create.html'
    form_class = AlbumForm
    model = Album
    success_url = reverse_lazy('gallery:photo-list')

    def form_valid(self, form):
        self.album = form.save(commit=False)
        self.album.author = self.request.user
        self.album.save()
        form.save_m2m()
        return self.get_success_url()

    def get_success_url(self):
        return redirect('webapp:album-view', pk=self.album.id)


class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = AlbumForm
    model = Album
    template_name = 'album/update.html'
    context_object_name = 'album'
    permission_required = 'webapp.change_album'

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()

    def get_success_url(self):
        return reverse('webapp:album-view', kwargs={'pk': self.kwargs.get('pk')})


class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    model = Album
    template_name = 'album/delete.html'
    context_object_name = 'object'
    permission_required = "webapp.delete_album"
    success_url = reverse_lazy('webapp:photo-list')

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()