from django.db import models
from django.db import models
from django.utils import timezone

import datetime

class Post(models.Model):
    title = models.CharField(max_length=140)
    post_text = models.TextField(default='')
    published_date = models.DateTimeField('date published')
    post_image = models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%D/')
    
    def __str__(self):
        return self.title
    
    def children(self):
        return Post.objects.filter(parent=self)
        
    
    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
    
    class Meta:
        verbose_name_plural = "Blog Posts"
        
class Comment(models.Model):
    comment_text = models.TextField(default='')
    published_date = models.DateTimeField('date published')
    parent = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE);