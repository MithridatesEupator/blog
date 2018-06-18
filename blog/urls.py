from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from blog.models import Entry

urlpatterns = [
    path('', ListView.as_view(queryset=Entry.objects.all().order_by("-date")[:25], template_name="blog/main.html"), name="blog"),
]
