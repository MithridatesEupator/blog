from django.shortcuts import render, get_object_or_404
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
    context = {
        "form" : form
    }
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('blog:index'))
    return render(request, "accounts/register.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user_login"))

def see_account(request, slug):
    user_obj = get_object_or_404(MyUser, username=slug)
    edit_form = EditProfile()
    current_user = request.user
    context = {
        "profile_user" : user_obj, "edit_form" : edit_form, "current_user" : current_user
    }
    return render(request, "accounts/profile.html", context)

def edit_profile(request, slug):
    if request.method == 'POST':
        edit_form = EditUser()
        current_user = request.user
        context = {
            "edit_form" : edit_form, "current_user" : current_user
        }
        return render(request, "accounts/edit.html", context)
    else:
        return HttpResponseRedirect(reverse('blog:index'))

def submit_changes(request, slug):
    if request.method == 'POST':
        edit_form = EditUser(request.POST, request.FILES)
        print(edit_form.errors)
        if edit_form.is_valid():
            user_obj = get_object_or_404(MyUser, username=slug)
            if edit_form.cleaned_data['username'] is not None:
                user_obj.username = edit_form.cleaned_data['username']
            if edit_form.cleaned_data['email'] is not None:
                user_obj.email = edit_form.cleaned_data['email']
            print(edit_form.cleaned_data['bio'])
            if edit_form.cleaned_data['bio'] is not None:
                user_obj.bio = edit_form.cleaned_data['bio']
            if edit_form.cleaned_data['profile_pic'] is not None:
                user_obj.profile_pic = edit_form.cleaned_data['profile_pic']
            user_obj.save()
    return HttpResponseRedirect(reverse('blog:index'))
    