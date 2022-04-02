from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile', verbose_name='Профиль')
    photo = models.ImageField(null=True, blank=True, upload_to='photos', verbose_name="Аватарка")

    def __str__(self):
        return f'Профиль: {self.user.username}'

    class Meta:
        db_table = 'Profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'