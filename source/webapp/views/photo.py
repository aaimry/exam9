from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views import View
import uuid
from webapp.models import Photo, UuidLink
from webapp.forms import PhotoForm


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'photos/index.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('-create_date')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(is_private=False)).exclude(album__is_private=True)
        return queryset


class PhotoView(LoginRequiredMixin, DetailView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'photos/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.object.author == self.request.user
        return context


class CreatePhotoView(LoginRequiredMixin, CreateView):
    template_name = 'photos/create.html'
    form_class = PhotoForm
    model = Photo
    success_url = reverse_lazy('webapp:index_photo')

    def get_form_kwargs(self):
        kwargs = super(CreatePhotoView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        self.photo = form.save(commit=False)
        self.photo.author = self.request.user
        self.photo.save()

        return self.get_success_url()

    def get_success_url(self):
        return redirect('webapp:view_photo', pk=self.photo.id)


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = PhotoForm
    model = Photo
    template_name = 'photos/update.html'
    context_object_name = 'photo'
    permission_required = 'webapp.change_photo'

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()

    def get_success_url(self):
        return reverse('webapp:view_photo', kwargs={'pk': self.kwargs.get('pk')})

    def get_form_kwargs(self):
        kwargs = super(PhotoUpdateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photos/delete.html'
    context_object_name = 'object'
    success_url = reverse_lazy('webapp:index_photo')
    permission_required = 'webapp.delete_photo'

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()


class GetPhotoByLink(View):

    def get(self, request, *args, **kwargs):
        context = {}
        uuid = kwargs.get('uuid')
        photo = Photo.objects.get(link__link=uuid)
        context['photo'] = photo
        return render(request, 'photos/view.html', context=context)


class GenerateLink(View):

    def get(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, id=kwargs.get('pk'))
        link = UuidLink.objects.create(photo=photo, link=str(uuid.uuid4()))
        return redirect('webapp:view_photo', pk=photo.id)
