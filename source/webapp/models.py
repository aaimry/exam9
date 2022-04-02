from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos', blank=False, null=False, verbose_name='Фото')
    description = models.CharField(max_length=100, blank=False, null=False, verbose_name='Описание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author', verbose_name='Автор')
    is_private = models.BooleanField(default=False, verbose_name='Приватность')
    album = models.ForeignKey('webapp.Album', on_delete=models.CASCADE, related_name="album", null=True, blank=True)

    def __str__(self):
        return f'{self.description} {self.author}'

    class Meta:
        db_table = 'Photos'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Album(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Название')
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Описание')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='album_author',
                                     verbose_name='Автор Альбома')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_private = models.BooleanField(default=False, verbose_name='Приватность')

    def __str__(self):
        return f'{self.title}{self.description} {self.author}'

    class Meta:
        db_table = 'Albums'
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
