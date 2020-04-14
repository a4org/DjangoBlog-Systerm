from django.contrib import admin
from .models import Comment
from DBlog.wadmin import wadminsite

# Register your models here.


@admin.register(Comment, site=wadminsite)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nick_name', 'content', 'website', 'created_time')
