from django.shortcuts import render
from django.urls import reverse
from .forms import *
from .models import *
from blog import views
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

def user_login(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect(reverse('blog:index'))
    return render(request, "accounts/login.html", {"form": form})

def user_register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('blog:index'))
    return render(request, "accounts/register.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user_login"))

def see_account(request, slug):
    pass