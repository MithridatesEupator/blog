from django.db import models
from django.db import models
from django.utils import timezone
from accounts.models import MyUser
import datetime




class Post(models.Model):
    title = models.CharField(max_length=140)
    post_text = models.TextField(default='')
    published_date = models.DateTimeField('date published')
    post_image = models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%D/')
    post_url = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    post_delete_status = models.BooleanField(default=False)
    post_likes = models.IntegerField(default=0) 
    poster = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Blog Posts"
        
class Comment(models.Model):
    comment_text = models.TextField(default='')
    published_date = models.DateTimeField('date published')
    parent = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE);
    comment_delete_status = models.BooleanField(default=False)
    commenter = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    comment_likes = models.IntegerField(default=0)

class Question(models.Model):
    question_text = models.CharField(max_length=240)
    published_date = models.DateTimeField(auto_now_add=True)

class Choice(models.Model):
    parent = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)