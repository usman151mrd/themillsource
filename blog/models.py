import datetime

from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class LifeStyleCities(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    editor = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='editor')
    post_date = models.DateTimeField(auto_now_add=True)
    schedule_time = models.DateTimeField(default=timezone.now)
    post_content = models.TextField()
    post_title = models.CharField(max_length=1000, null=False)
    post_status = models.CharField(max_length=100)
    post_modified = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, related_name='category_id', on_delete=models.CASCADE)
    city = models.ForeignKey(LifeStyleCities, related_name='city_id', on_delete=models.CASCADE, null=True)
    tags = models.CharField(max_length=500, null=True)
    keywords = models.CharField(max_length=500, null=True)
    slug = models.SlugField(max_length=200)
    meta_title = models.CharField(max_length=500)
    meta_description = models.TextField(null=True)
    feature_image_url = models.ImageField(max_length=1000)
    seen = models.BigIntegerField()

    def was_published_recently(self):
        return self.schedule_time >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.post_title


class PressReleaseForm(models.Model):
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, validators=[validators.EmailValidator])
    logo = models.ImageField()
    image = models.ImageField()
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=25)
    description = models.TextField()
    discount_description = models.TextField()
    release_date = models.DateField()
    sample = models.FileField()
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()


class NewsSource(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
