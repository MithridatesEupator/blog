from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.make_post, name='make_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('delete-comment/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('post/<slug:slug>/', views.see_post, name='see_post'),
    path('post-vote/<int:vote>/<int:pk>/', views.post_vote, name="post_vote"),
    path('comments/<int:pk>/', views.make_comment, name='make_comment'),
    path('comment-vote/<int:vote>/<int:pk>/', views.comment_vote, name="comment_vote"),
    path('log-in/', views.see_log_in, name="see_log_in")   
]