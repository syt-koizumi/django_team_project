from django.db import models

# Create your models here.
class ThisWeekMovies(models.Model):
    title = models.CharField("映画名",max_length=50)
    day = models.DateField("公開日")
    youtube = models.TextField("youtubeの動画id(例 https://www.youtube.com/watch?v=pjXW-hDfUzc の pjXW-hDfUzcの部分)",max_length=10000)
    overview = models.TextField("映画概要",max_length=10000)
 
    def __str__(self):
          return self.title


