
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("toppage.urls")),
    path("accounts/",include("accounts.urls")),
    path("mypage/",include("mypage.urls")),
    path("movie/",include("movie.urls")),
    path("usersearch/",include("usersearch.urls")),
]
