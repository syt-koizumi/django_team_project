# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from .models import Comment, Like
from movie.models import MyMovieModel
from .forms import CommentForm, MovieFilterForm
from django.contrib.auth.mixins import LoginRequiredMixin

class CommentView(LoginRequiredMixin,View):
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
    
def like_comment(request, comment_id):
    if request.method == "POST":
        comment = get_object_or_404(Comment, id=comment_id)

        user = request.user

        # 既に「いいね」しているか確認
        existing_like = Like.objects.filter(user=user, comment=comment)
        if existing_like:
            # 「いいね」を取り消す
            existing_like.delete()
            comment.likes -= 1
            comment.save()
            return JsonResponse({'likes': comment.likes, 'message': 'Like removed'})
        else:
            # 「いいね」を追加
            Like.objects.create(user=user, comment=comment)
            comment.likes += 1
            comment.save()
            return JsonResponse({'likes': comment.likes, 'message': 'Like added'})


    return JsonResponse({'error': 'Invalid request'}, status=400)
