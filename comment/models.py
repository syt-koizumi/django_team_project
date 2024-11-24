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
    imagepath = models.CharField(verbose_name="映画の画像", max_length = 1000)
    user = models.ForeignKey(CustomUser,verbose_name="追加したユーザー", on_delete=models.CASCADE)
    comment = models.CharField(verbose_name="コメント", max_length = 1000)
    rating = models.IntegerField(choices=SCORE_CHOICES)
    date = models.DateTimeField(auto_now_add=True, verbose_name="投稿日")
    likes = models.IntegerField(default=0)

    def __str__(self):
       return f'{self.movie_name.name} - {self.user.username}'
    

class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_likes')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_comment')

    class Meta:
        unique_together = ('user', 'comment')