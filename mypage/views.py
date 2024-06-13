from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DeleteView
from movie.models import MyMovieModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

    
    
class MylistView(LoginRequiredMixin, TemplateView):
    template_name = 'mypage/mylist.html'

    def get(self, request):

        MyMovieModel_data = MyMovieModel.objects.filter(createUser=self.request.user)
        context = {
            'MyMovieModel_data': MyMovieModel_data
        }
        return render(request, 'mypage/mylist.html', context)
    
    
class DeleteView(LoginRequiredMixin, DeleteView):
    model = MyMovieModel
    template_name = 'mypage/delete.html'
    success_url = reverse_lazy('mypage:mylist')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user == self.object.createUser:
            return super().get(request, *args, **kwargs)
        else:
            #return super().get(request, *args, **kwargs)
            raise PermissionDenied('nooooooo')
        
    