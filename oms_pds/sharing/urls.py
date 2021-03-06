from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('oms_pds.sharing.views',
    (r'^edit/', 'edit'),
    (r'^update/', 'update'),
    (r"^overview/", direct_to_template, { "template": "sharing/mock.html" }),
)
