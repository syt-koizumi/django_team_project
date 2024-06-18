from django import forms
from .models import Comment
from movie.models import MyMovieModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['movie_name','score', 'comment']


class MoviePullDownForm(forms.ModelForm):
    class Meta:
        model = MyMovieModel
        fields = ('name',)
