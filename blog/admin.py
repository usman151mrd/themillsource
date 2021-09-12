from django.contrib import admin
from blog.models import *


class PostModelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post Information', {'fields': ['author', 'editor', 'schedule_time', 'post_content', 'post_title',
                                         'post_status', 'category', 'city', 'slug', 'feature_image_url']}),
        ('SEO information', {'fields': ['tags', 'keywords', 'meta_title', 'meta_description']}),
    ]
    prepopulated_fields = {'slug': ('post_title',), }
    list_display = ('post_title', 'post_status', 'slug', 'author')


admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
admin.site.register(PressReleaseForm)

admin.site.register(NewsSource)
