from django.db import models
from accounts.models import CustomUser
from movie.models import MyMovieModel

SCORE_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]

class Comment(models.Model):
    # movie_nameとimagepathのリレーションに関しては自信なし。Foreignkeyかも
    movie_name = models.ManyToManyField(MyMovieModel, verbose_name="映画名", related_name='movie_comments')
    # overview = models.CharField("映画の概要", max_length=10000)
    imagepath = models.ManyToManyField(MyMovieModel, verbose_name="映画の画像パス", related_name='imagepath_comments')
    createUser = models.ManyToManyField(CustomUser,verbose_name="追加したユーザー")
    comment = models.CharField(verbose_name="コメント", max_length = 1000)
    score = models.PositiveSmallIntegerField(verbose_name="レビュースコア", choices=SCORE_CHOICES, default='3')
    date = models.DateField(verbose_name="投稿日", auto_now_add=True)
    
    def __str__(self):
       return self.movie_name