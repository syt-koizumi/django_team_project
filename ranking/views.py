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
        
        RankingMovie = MyMovieModel.objects.values('imagepath', 'name', 'overview').annotate(movie_count=Count('createUser')).order_by('-movie_count')
        
        now_rank = 1
        kaburi_count = 0
        last_score = None
        result_rank = []

        for movie in RankingMovie:
            score = movie['movie_count']
            if last_score is not None and score != last_score:
                now_rank += kaburi_count
                kaburi_count = 0
            last_score = score
            movie['rank'] = now_rank
            result_rank.append(movie)
            kaburi_count += 1

        return result_rank[:10]

        # return render(self.request,'ranking/ranking.html',context)
