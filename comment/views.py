
# views.py
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Comment
from movie.models import MyMovieModel
from .forms import CommentForm

class CommentView(View):
    def get(self, request):
        form = CommentForm(user=request.user)
        comments = Comment.objects.all().order_by('-date')
        return render(request, 'comment/comments.html', {'form': form, 'comments': comments})

    def post(self, request):
        form = CommentForm(request.POST, user=request.user)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.imagepath = comment.movie_name
            comment.save()
            return redirect('/comment')
        comments = Comment.objects.all().order_by('-date')
        return render(request, 'comment/comments.html', {'form': form, 'comments': comments})
   
