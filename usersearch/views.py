from django.views.generic import FormView, DetailView, ListView
from accounts.models import CustomUser
from movie.models import MyMovieModel
from .forms import UserSearchForm

class UserSearchView(FormView):
    template_name = 'usersearch/userlist.html'
    form_class = UserSearchForm
    context_object_name = 'users'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        users = CustomUser.objects.filter(username__icontains=username)
        print(f"Searching for users with username containing '{username}': {users}")
        return self.render_to_response(self.get_context_data(users=users))
    

class UserMoviesView(DetailView):
    model = CustomUser
    template_name = 'usersearch/userlist_result.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = "aaaaa"
        context['movies'] = MyMovieModel.objects.filter(createUser=self.object)
        return context

