from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

from . import views

urlpatterns = [
           url(r'^(?P<slug>[\w-]+)/$', views.page_detail, name='page_detail'),
]
