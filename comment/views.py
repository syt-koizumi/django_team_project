from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Comment
from .forms import CommentForm,MoviePullDownForm

class CommentView(ListView):
    model = Comment
    template_name = 'comment/comment.html'
    context_object_name = 'comments'
    form_class = MoviePullDownForm

    def get_queryset(self):
        UserComments = Comment.objects.all().order_by('-date')

        return UserComments

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context
    

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.save()
        return redirect('comment')