# forms.py
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

# class MovieFilterForm(forms.Form):
#     movie_name = forms.ModelChoiceField(
#         queryset=MyMovieModel.objects.filter(movie_comments__isnull=False).distinct("name"),
#         required=False,
#         label='Filter by Movie'
#     )

class MovieFilterForm(forms.Form):
    movie_name = forms.ChoiceField(
        choices=[('', '---------')] + [(movie['name'], movie['name']) for movie in MyMovieModel.objects.filter(movie_comments__isnull=False).values('name').distinct()],
        required=False,
        label='Filter by Movie'
    )