# from django.contrib.auth.models import User
# from django.db import models
#
#
# class DownloadLink(models.Model):
#     user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL, verbose_name='Пользователь')
#     link = models.SlugField(max_length=400, unique=True, db_index=True, verbose_name="URL")
#     title = models.CharField(max_length=255, verbose_name="Заголовок")
#     content = models.TextField(blank=True, verbose_name="Текст статьи")
#     photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")


