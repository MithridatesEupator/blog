from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Post
from datetime import datetime
from django.utils import timezone

# Create your views here.
def index(request):
    blog_post_list = Post.objects.all()[:5]
    context = {
        "blog_post_list": blog_post_list,
    }
    return render(request, 'blog/main.html', context)


def details(request, id):
    individual_post = Posts.objects.get(id=id)
    context = {
        "individual_post" : individual_post
    }
    return render(request, 'blog/detail.html', context)

def make_post(request):
    #return render(request, 'blog/upload_post.html')
    if request.method == 'GET':
        return render(request, 'blog/upload_post.html', {})
    elif request.method == 'POST':
        post = Post(title=request.POST['title'], post_text=request.POST['content'], published_date=timezone.now())
        post.save()
        return HttpResponseRedirect(reverse('index'))
        #return render(request, 'blog/upload_post.html', {})
        
def delete_post(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('index'))
    elif request.method == 'POST':
        delete_id = int(request.POST['delete_id'])
        post = SomeModel.objects.get(id=delete_id)
        post.delete()
        return HttpResponseRedirect(reverse('index'))
