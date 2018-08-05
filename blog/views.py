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
from django.template.defaultfilters import slugify 

# Create your views here.
def index(request):
    blog_post_list = Post.objects.all()[::-1]
    comment_list = Comment.objects.all()
    current_user = request.user
    form_post = make_post_form()
    form_comment = make_comment_form()
    context = {
        "blog_post_list" : blog_post_list, "form_post" : form_post, "form_comment" : form_comment, "comment_list" : comment_list, "current_user" : current_user
    }
    return render(request, 'blog/main.html', context)


def see_post(request, slug):
    individual_post = get_object_or_404(Post, post_url=slug)
    comment_list = Comment.objects.all()
    form_post = make_post_form()
    form_comment = make_comment_form()
    form_delete_post = delete_post_form()
    form_delete_comment = delete_comment_form()
    current_user = request.user
    context = {
        "individual_post" : individual_post, "comment_list" : comment_list, "form_post" : form_post, "form_comment" : form_comment,
        "form_delete_post" : form_delete_post, "form_delete_comment" : form_delete_comment, "current_user" : current_user
    }
    return render(request, 'blog/individual_post.html', context)

def make_post(request):
    post_user = request.user
    if request.method == 'GET':
        return render(request, 'blog/upload_post.html', {})
    elif request.method == 'POST':
        form_post = make_post_form(request.POST, request.FILES)
        print(form_post.errors)
        if form_post.is_valid():
            if post_user.is_staff:
                title_pass=form_post.cleaned_data['title']
                post_text_pass = form_post.cleaned_data['post_text']
                post_image_pass = form_post.cleaned_data['post_image']
                post_slug_pass = slugify(title_pass)
                post = Post(title=title_pass, post_text=post_text_pass, published_date=timezone.now(), post_image=post_image_pass, post_url=post_slug_pass, poster=post_user)
                post.save()
        return HttpResponseRedirect(reverse('blog:index'))
    
def make_comment(request, pk):
    comment_user = request.user
    if request.method == 'GET':
        return render(request, 'blog/upload_post.html', {})
    elif request.method == 'POST':
        form_comment = make_comment_form(request.POST, request.FILES)
        if form_comment.is_valid():
            if comment_user.is_staff:
                comment_text_pass = form_comment.cleaned_data['comment_text']
                parent_post = get_object_or_404(Post, pk=pk)
                comment = Comment(comment_text=comment_text_pass, published_date=timezone.now(), parent=parent_post, commenter=comment_user)  
                comment.save()
                slug_pass= parent_post.post_url
                return HttpResponseRedirect(reverse('blog:see_post', kwargs={'slug': slug_pass}))
    
def delete_post(request, slug):
    post = get_object_or_404(Post, post_url=slug)
    if request.method == 'POST':
        delete_form = delete_post_form(request.POST, request.FILES)
        if delete_form.is_valid:
            post.post_delete_status = True;
            post.save();
    return HttpResponseRedirect(reverse('blog:index'))

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    parent_post = get_object_or_404(Post, pk=comment.parent_id)
    comment.comment_delete_status = True;
    comment.save();
    slug_pass= parent_post.post_url
    return HttpResponseRedirect(reverse('blog:see_post', kwargs={'slug': slug_pass}))

def comment_vote(request, vote, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.comment_likes += 1
    comment.save()
    parent_post = get_object_or_404(Post, pk=comment.parent_id)
    slug_pass= parent_post.post_url
    return HttpResponseRedirect(reverse('blog:see_post', kwargs={'slug': slug_pass}))
    
def post_vote(request, vote, pk):
    post = get_object_or_404(Post, pk=pk)
    post.post_likes += 1
    post.save()
    slug_pass= post.post_url
    return HttpResponseRedirect(reverse('blog:see_post', kwargs={'slug': slug_pass}))

def see_log_in(request):
    form_login = log_in_form()
    content = {
        "form_login" : form_login
    }
    return render(request, 'blog/login.html', content)
    
