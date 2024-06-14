from django import forms

class UserSearchForm(forms.Form):
    username = forms.CharField(label='ユーザー名')
    #results1 = forms.CharField(label="検索結果")



from accounts.models import CustomUser
class CustomUserForm(forms.ModelForm):
      class Meta:
          model = CustomUser
          fields = ('username',)