from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView, ListView
)
from django.urls import reverse, reverse_lazy

from webapp.models import Photo, Album
from webapp.forms import AlbumForm


class AlbumView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'albums/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Photo.objects.filter(album=self.object).exclude(is_private=True)
        context['is_author'] = self.object.author == self.request.user
        return context


class AlbumListView(ListView):
    model = Album
    context_object_name = "albums"
    template_name = 'partial/album_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(is_private=False))
        return queryset


class CreateAlbumView(LoginRequiredMixin, CreateView):
    template_name = 'albums/create.html'
    form_class = AlbumForm
    model = Album
    success_url = reverse_lazy('webapp:index_photo')

    def form_valid(self, form):
        self.album = form.save(commit=False)
        self.album.author = self.request.user
        self.album.save()
        form.save_m2m()
        return self.get_success_url()

    def get_success_url(self):
        return redirect('webapp:view_album', pk=self.album.id)


class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = AlbumForm
    model = Album
    template_name = 'albums/update.html'
    context_object_name = 'album'
    permission_required = 'webapp.change_album'

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()

    def get_success_url(self):
        return reverse('webapp:view_album', kwargs={'pk': self.kwargs.get('pk')})


class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    model = Album
    template_name = 'albums/delete.html'
    context_object_name = 'object'
    permission_required = "webapp.delete_album"
    success_url = reverse_lazy('webapp:index_photo')

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()