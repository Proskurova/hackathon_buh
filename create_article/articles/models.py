from django.contrib.auth.models import User
from django.db import models


class DownloadLink(models.Model):
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL, verbose_name='Пользователь')
    link = models.URLField(db_index=True, verbose_name="Ссылка")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    time = models.FloatField(verbose_name="Время воспроизведения видео")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    video = models.FileField(upload_to='videos/', verbose_name="Видео")


