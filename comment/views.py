# views.py
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Comment
from movie.models import MyMovieModel
from .forms import CommentForm, MovieFilterForm

class CommentView(View):
    def get(self, request):
        comment_form = CommentForm(user=request.user)
        filter_form = MovieFilterForm(request.GET or None)
        comments = Comment.objects.all().order_by('-date')

        if filter_form.is_valid() and filter_form.cleaned_data['movie_name']:
            comments = comments.filter(movie_name=filter_form.cleaned_data['movie_name'])

        return render(request, 'comment/comment.html', {
            'comment_form': comment_form,
            'filter_form': filter_form,
            'comments': comments
        })

    def post(self, request):
        comment_form = CommentForm(request.POST, user=request.user)
        filter_form = MovieFilterForm(request.GET or None)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            movie = comment_form.cleaned_data['movie_name']
            comment.imagepath = movie.imagepath
            comment.save()
            return redirect('/comment')

        comments = Comment.objects.all().order_by('-date')
        if filter_form.is_valid() and filter_form.cleaned_data['movie_name']:
            comments = comments.filter(movie_name=filter_form.cleaned_data['movie_name'])

        return render(request, 'comment/comment.html', {
            'comment_form': comment_form,
            'filter_form': filter_form,
            'comments': comments
        })
