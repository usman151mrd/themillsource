from django.contrib import admin

# Register your models here.
from blog.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PressReleaseForm)

admin.site.register(NewsSource)
