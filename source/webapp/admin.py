from django.contrib import admin
from webapp.models import Photo, Album


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'description', 'author', 'create_date', 'is_private', 'album']
    fields = ['photo', 'description', 'author', 'is_private', 'album']
    readonly_fields = ['id', 'create_date']


admin.site.register(Photo, PhotoAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'author', 'is_private', 'create_date']
    fields = ['title', 'description', 'author', 'is_private']
    readonly_fields = ['id', 'create_date']


admin.site.register(Album, AlbumAdmin)
