from django.contrib import admin
from .models import Post, Category, Tag
from django.contrib.admin import AdminSite
from DBlog.wadmin import wadminsite
from DBlog.wadmin_base import BaseOwnerAdmin


@admin.register(Post, site=wadminsite)
class PostAdmin(BaseOwnerAdmin):
    list_display = ['title', 'owner', 'created_time', 'status']
    search_fields = ['title', 'Category__name']
    fields = (
        ('title', 'Category'),
        'disc',
        'status',
        'content',
        'tag',
    )
    list_filter = ['Category']
    show_full_result_count = False
    actions_on_top = True


@admin.register(Category, site=wadminsite)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'is_nav', 'create_time']
    fields = ['name', 'status', 'is_nav']


@admin.register(Tag, site=wadminsite)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')
