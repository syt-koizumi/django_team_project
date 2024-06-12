from django.db import models
from accounts.models import CustomUser

class MyMovieModel(models.Model):
    name = models.CharField('映画名', max_length=200)
    overview = models.CharField('映画の概要', max_length=10000)
    imagepath = models.CharField("映画の画像パス",max_length = 10000)
    createUser = models.ManyToManyField(CustomUser,verbose_name="追加したユーザー")
    def __str__(self):
       return self.name
