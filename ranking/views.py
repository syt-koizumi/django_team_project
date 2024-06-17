from django.shortcuts import render
from django.views.generic import TemplateView
from movie.models import MyMovieModel
from django.views.generic import ListView
from django.db.models import Count

    
# class MovieRankingView(ListView):
#     model = MyMovieModel
#     template_name = 'ranking/ranking.html'
#     context_object_name = 'movies'

#     def get_queryset(self):
#         return MyMovieModel.objects.annotate(user_count=Count('createUser')).order_by('-user_count')

class MovieRankingView(ListView):
    model = MyMovieModel
    template_name = 'ranking/ranking.html'
    context_object_name = 'movies'

    def get_queryset(self):
        #MyMovieModelからデータを取得してAllMovie変数に格納
        # AllMovie = MyMovieModel.objects.all()
        
        RankingMovie = MyMovieModel.objects.values('imagepath', 'name', 'overview').annotate(movie_count=Count('createUser')).order_by('-movie_count')[0:10]

        return RankingMovie
