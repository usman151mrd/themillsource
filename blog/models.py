import datetime
from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


def post_upload_to(instance, filename):
    return 'blog/post/{filename}'.format(filename=filename)


def logo_upload_to(instance, filename):
    return 'blog/post/{filename}'.format(filename=filename)


def ns_upload_to(instance, filename):
    return 'blog/source/{filename}'.format(filename=filename)


def wfu_upload_to(instance, filename):
    return 'blog/write4us/{filename}'.format(filename=filename)


def press_upload_to(instance, filename):
    return 'blog/press/{filename}'.format(filename=filename)


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    editor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='editor')
    post_date = models.DateTimeField(auto_now_add=True)
    schedule_time = models.DateTimeField(default=timezone.now)
    post_content = models.TextField()
    post_title = models.CharField(max_length=1000, null=False)
    post_status = models.CharField(max_length=20,  choices=options, default='published')
    post_modified = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, related_name='category_id', on_delete=models.CASCADE)
    city = models.CharField(max_length=100, null=True, blank=True)
    tags = models.CharField(max_length=500, null=True, blank=True)
    keywords = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=200)
    meta_title = models.CharField(max_length=500, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    feature_image_url = models.ImageField(_("Image"), upload_to=post_upload_to, default='blog/post/default.jpg')
    seen = models.BigIntegerField(default=0)
    objects = models.Manager()  # default manager

    class Meta:
        ordering = ('-post_date',)

    def __str__(self):
        return self.post_title

    def published(self):
        return self.schedule_time < timezone.now() and self.post_status == 'published'


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=250)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name


class PressRelease(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, validators=[validators.EmailValidator])
    image = models.ImageField(_("Image"), upload_to=press_upload_to, default='blog/press/default.jpg')
    heading = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.heading


class WriteForUs(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, validators=[validators.EmailValidator])
    image = models.ImageField(_("Image"), upload_to=wfu_upload_to, default='blog/write4us/default.jpg')
    heading = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.heading


class NewsSource(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(_("Image"), upload_to=ns_upload_to, default='blog/source/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')
    url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
