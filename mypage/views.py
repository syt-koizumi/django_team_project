from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from movie.models import MyMovieModel
from django.contrib.auth.mixins import LoginRequiredMixin

    
    
class MylistView(LoginRequiredMixin, TemplateView):
    template_name = 'mypage/mylist.html'

    def get(self, request):

        MyMovieModel_data = MyMovieModel.objects.filter(createUser=self.request.user)
        context = {
            'MyMovieModel_data': MyMovieModel_data
        }
        return render(request, 'mypage/mylist.html', context)

    # def get(request, id):

    #     MyMovieModel_data = get_object_or_404(MyMovieModel, pk = id)
    #     context = {
    #         'MyMovieModel_data': MyMovieModel_data
    #     }
        
    #     return render(request, 'mypage/mylist.html', context)
