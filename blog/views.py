from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Post
from datetime import datetime
from django.utils import timezone
from .forms import *
from django import forms
from django.contrib import messages

# Create your views here.
def index(request):
    blog_post_list = Post.objects.all()[::-1]
    comment_list = Comment.objects.all()
    form_post = make_post_form()
    form_comment = make_comment_form()
    context = {
        "blog_post_list" : blog_post_list, "form_post" : form_post, "form_comment" : form_comment, "comment_list" :
        comment_list
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
        form_post = make_post_form(request.POST, request.FILES)
        print(form_post.errors)
        if form_post.is_valid():
            title_pass=form_post.cleaned_data['title']
            post_text_pass = form_post.cleaned_data['post_text']
            post_image_pass = form_post.cleaned_data['post_image']
            post = Post(title=title_pass, post_text=post_text_pass, published_date=timezone.now(), post_image=post_image_pass)
            post.save()
        return HttpResponseRedirect(reverse('index'))
    
def make_comment(request, pk):
    if request.method == 'GET':
        return render(request, 'blog/upload_post.html', {})
    elif request.method == 'POST':
        form_comment = make_comment_form(request.POST, request.FILES)
        if form_comment.is_valid():
            comment_text_pass = form_comment.cleaned_data['comment_text']
            parent_post = Post.objects.get(pk=pk)
            comment = Comment(comment_text=comment_text_pass, published_date=timezone.now(), parent=parent_post)        
            comment.save()
        return HttpResponseRedirect(reverse('index'))
    
def delete_post(request, pk):
    template = 'blog/delete_post.html'
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        form = delete_post_form(request.POST, instance=post)
        comment_list = Comment.objects.all()
        if form.is_valid():
            post.delete()
            for comment in comment_list:
                if comment.parent_id == pk:
                    comment.delete()
    else: 
        form = delete_post_form(instance=post)
    return HttpResponseRedirect(reverse('index'))
