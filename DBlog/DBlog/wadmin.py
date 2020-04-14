from django.contrib.admin.sites import AdminSite


class Wadminsite(AdminSite):
    site_header = 'DBlog Adminstration'
    site_title = 'DBlog Adminstration'
    index_title = 'Home'


wadminsite = Wadminsite(name='wadmin')
