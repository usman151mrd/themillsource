from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blog.models import *


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('post_content',)
    fieldsets = [
        ('Post Information', {'fields': ['author', 'editor', 'schedule_time', 'post_content', 'post_title',
                                         'post_status', 'category', 'city', 'slug', 'feature_image_url']}),
        ('SEO information', {'fields': ['tags', 'keywords', 'meta_title', 'meta_description']}),
    ]
    prepopulated_fields = {'slug': ('post_title',), }
    list_display = ('post_title', 'post_status', 'slug', 'author')


class NewsSourceAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(PressRelease)
admin.site.register(WriteForUs)

admin.site.register(NewsSource, NewsSourceAdmin)


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}  # new


class CommentsAdmin(SummernoteModelAdmin):
    summernote_fields = ('comment',)


admin.site.register(Comments, CommentsAdmin)
admin.site.register(Article, ArticleAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent',)


admin.site.register(Menu, MenuAdmin)
