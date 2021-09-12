import datetime
from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.utils import timezone
from django_quill.fields import QuillField
from django.utils.translation import gettext_lazy as _


def post_upload_to(instance, filename):
    return 'blog/post/{filename}'.format(filename=filename)


def ns_upload_to(instance, filename):
    return 'blog/source/{filename}'.format(filename=filename)


def logo_upload_to(instance, filename):
    return 'blog/press/{filename}'.format(filename=filename)


def press_upload_to(instance, filename):
    return 'blog/logo/{filename}'.format(filename=filename)


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    editor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='editor')
    post_date = models.DateTimeField(auto_now_add=True)
    schedule_time = models.DateTimeField(default=timezone.now)
    post_content = QuillField(default='')
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


class PressReleaseForm(models.Model):
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, validators=[validators.EmailValidator])
    logo = models.ImageField(_("logo"), upload_to=logo_upload_to)
    image = models.ImageField(_("Image"), upload_to=press_upload_to)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=25)
    description = QuillField(default='')
    discount_description = QuillField(default='')
    release_date = models.DateField()
    sample = models.FileField()
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.company_name


class NewsSource(models.Model):
    title = models.CharField(max_length=500)
    description = QuillField(default='')
    url = models.URLField()
    image = models.ImageField(_("Image"), upload_to=ns_upload_to, default='blog/source/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
