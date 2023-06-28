from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, FormView

from articles.forms import *
from articles.models import *

from pytube import YouTube


class ArticlesHome(FormView):
    form_class = DownloadLinkForm
    template_name = 'articles/home.html'
    success_url = reverse_lazy('home')


def processing(request):
    if request.method == 'POST':
        link = request.POST.get("link")
        yt = YouTube(link)
        time_video = round(yt.length / 60, 2)
        title_article = yt.title
        ys = yt.streams.get_highest_resolution()
        ys.download()
        context = {
            'time_video': time_video,
            'title_article': title_article
        }
        return render(request, template_name='articles/process.html', context=context)
    return render(request, template_name='articles/home.html')


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

