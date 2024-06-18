from django import forms
from .models import Comment
from movie.models import MyMovieModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['movie_name', 'comment', 'rating']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['movie_name'].queryset = MyMovieModel.objects.filter(createUser=user)
