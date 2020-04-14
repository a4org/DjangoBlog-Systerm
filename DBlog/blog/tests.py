from __future__ import unicode_literals
from pprint import pprint as pp
from django.test import TestCase
from django.db import connection
from django.test.utils import override_settings
from django.contrib.auth.models import User
from .models import Category, Post, Tag
from django.db.models import F, Count, Sum
# Create your tests here

class TastCategory(TestCase):
    @override_settings(DEBUG=True)
    def setUp(self):
        self.user = user = User.objects.create_user('wange', 's1239587@ouhk.edu.hk', '88888888')
        Category.objects.bulk_create([
            Category(name='cate_bulk_%s' % i, owner=user)
            for i in range(10)
        ])

    @override_settings(DEBUG=True)
    def test_filter(self):
        category = Category.objects.filter(id=1).update(status=F('status')+1)
        print(Category.objects.filter(owner__username__startswith="wan"))
        users = User.objects.filter(username="wange").annotate(cate_count=Count('category'))
        user = users[0]
        print(user.cate_count)
        pp(connection.queries)
