from django.db import models
from django.db import models
from django.utils import timezone

import datetime

class Post(models.Model):
    title = models.CharField(max_length=140)
    post_text = models.TextField()
    #post_image = models.ImageField()
    published_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Blog Posts"

