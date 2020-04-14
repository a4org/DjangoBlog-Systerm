# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = [
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    ]

    title = models.CharField(max_length=255, verbose_name="标题")
    disc = models.CharField(max_length=255, blank=True, verbose_name="摘要")
    content = models.TextField(verbose_name = "正文", help_text = "正文必须为markdown格式")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name="状态")
    tag = models.ManyToManyField('Tag', verbose_name ="标签")
    Category = models.ForeignKey('Category', on_delete = models.CASCADE, verbose_name = "分类")
    owner = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "作者")
    created_time = models.DateTimeField(auto_now_add = True, verbose_name = "创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ['-id']

class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name = "名称")
    status = models.PositiveIntegerField(default = STATUS_NORMAL, choices = STATUS_ITEMS, verbose_name = "状态")
    is_nav = models.BooleanField(default=False, verbose_name = "是否设置为导航")
    owner = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "作者")
    create_time = models.DateTimeField(auto_now_add = True, verbose_name = "创建时间")

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = verbose_name_plural = "分类"
        ordering = ('id', 'create_time')

class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除"),
    )

    name = models.CharField(max_length = 10, verbose_name = "名称")
    status = models.PositiveIntegerField(default = STATUS_NORMAL, choices = STATUS_ITEMS, verbose_name = "状态")
    owner = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "作者")
    created_time = models.DateTimeField(auto_now_add = True, verbose_name = "创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '标签'

