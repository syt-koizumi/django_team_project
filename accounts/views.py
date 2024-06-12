from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm, CustomUserCreationForm,LoginAuthenticationForm
from .models import CustomUser
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView


class CustomAccountCreationView(generic.CreateView):
    Model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = '/accounts/custom_accounts_create'

class Login(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginAuthenticationForm
    


class Logout(LogoutView):
    template_name = 'accounts/logout.html'
    #next_page = '/accounts/login.html'


class Home(TemplateView):
    template_name = 'accounts/home.html'

