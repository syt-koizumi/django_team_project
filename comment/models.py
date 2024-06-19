from django.db import models
from accounts.models import CustomUser
from movie.models import MyMovieModel
from datetime import datetime

SCORE_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]

class Comment(models.Model):
    # movie_nameとimagepathのリレーションに関しては自信なし。Foreignkeyかも
    movie_name = models.ForeignKey(MyMovieModel, verbose_name="映画名", related_name='movie_comments', on_delete=models.CASCADE)
    # overview = models.CharField("映画の概要", max_length=10000)
    imagepath = models.ForeignKey(MyMovieModel, verbose_name="映画の画像パス", related_name='imagepath_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,verbose_name="追加したユーザー", on_delete=models.CASCADE)
    comment = models.CharField(verbose_name="コメント", max_length = 1000)
    rating = models.IntegerField(choices=SCORE_CHOICES)
    date = models.DateTimeField(default=datetime.now(), verbose_name="投稿日")
    def __str__(self):
       return f'{self.movie_name.name} - {self.user.username}'