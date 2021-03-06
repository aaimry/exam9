# Generated by Django 4.0.3 on 2022-04-02 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0002_uuidlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumFav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Избранный Альбом',
                'verbose_name_plural': 'Избранные Альбомы',
            },
        ),
        migrations.CreateModel(
            name='PhotoFav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Избранная Фотография',
                'verbose_name_plural': 'Избранные Фотографии',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='fav',
            field=models.ManyToManyField(through='webapp.AlbumFav', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='fav',
            field=models.ManyToManyField(through='webapp.PhotoFav', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photofav',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_fav', to='webapp.photo', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='photofav',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_fav', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='albumfav',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_fav', to='webapp.album', verbose_name='Альбом'),
        ),
        migrations.AddField(
            model_name='albumfav',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_fav', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
