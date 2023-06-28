from django.urls import path, re_path

from articles.views import *

urlpatterns = [
    path('', ArticlesHome.as_view(), name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('process/', processing, name='process')
]