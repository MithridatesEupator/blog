from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Post
from datetime import datetime
from django.utils import timezone
from .forms import make_post_form, delete_post_form
from django import forms
from django.contrib import messages

# Create your views here.
def index(request):
    blog_post_list = Post.objects.all()[:5]
    form_post = make_post_form()
    context = {
        "blog_post_list": blog_post_list, "form_post": form_post
    }
    return render(request, 'blog/main.html', context)


def details(request, id):
    individual_post = Posts.objects.get(id=id)
    context = {
        "individual_post" : individual_post
    }
    return render(request, 'blog/detail.html', context)

def make_post(request):
    if request.method == 'GET':
        return render(request, 'blog/upload_post.html', {})
    elif request.method == 'POST':
        form_post = make_post_form(data=request.POST)
        if form_post.is_valid():
            title_pass=form_post.cleaned_data['title']
            post_text_pass=form_post.cleaned_data['post_text']
            print(post_text_pass)
            post = Post(title=title_pass, post_text=post_text_pass, published_date=timezone.now())
            post.save()
        return HttpResponseRedirect(reverse('index'))
        
def delete_post(request, pk):
    template = 'blog/delete_post.html'
    post = get_object_or_404(Post, pk=pk)
    #need to replace GET with POST; not very safe
    if request.method == 'GET':
        form = delete_post_form(request.POST, instance=post)
        if form.is_valid():
            post.delete()
    else: 
        form = delete_post_form(instance=post)
    return HttpResponseRedirect(reverse('index'))