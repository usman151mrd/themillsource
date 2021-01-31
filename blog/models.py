from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.CharField(max_length=500, null=False)
    editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='editor', default=1)
    post_date = models.DateTimeField(auto_now_add=True)
    schedule_time = models.DateTimeField(default=timezone.now)
    post_content = models.TextField()
    post_title = models.CharField(max_length=1000, null=False)
    post_status = models.CharField(max_length=100)
    post_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.CharField(max_length=500,null=True)
    keywords = models.CharField(max_length=500,null=True)
    slug = models.SlugField()
    meta_title = models.CharField(max_length=500)
    meta_description = models.TextField(null=True)
    feature_image_url = models.ImageField()

    def __str__(self):
        return self.post_title
