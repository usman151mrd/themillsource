from django.contrib import admin

# Register your models here.
from blog.models import *

admin.site.register(Post)
admin.site.register(Category)

