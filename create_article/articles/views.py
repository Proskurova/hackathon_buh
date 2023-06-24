from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, ListView

from articles.forms import *
from articles.models import *

from pytube import YouTube


class ArticlesHome(TemplateView):
    form_class = DownloadLink
    template_name = 'articles/home.html'


class ProcessArticles(TemplateView):
    form_class = DownloadLink
    template_name = 'articles/process.html'

    def playback_time(self, link):
        yt = YouTube(link)
        link_video = round(yt.length / 60, 2)
        return link_video


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'articles/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'articles/register.html'
    success_url = reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

