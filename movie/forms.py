from django import forms

class MovieSearchForm(forms.Form):
    movie_name = forms.CharField(label='映画名')
    #results1 = forms.CharField(label="検索結果")