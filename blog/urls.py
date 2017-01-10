from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

from . import views

urlpatterns =[
       # url(r'^$', views.PostListView.as_view(), name='post_list'),
       url(r'^post/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
       url(r'^$', views.post_list, name='post_list'),
       url(r'^search/$', views.post_search, name='post_search'),
]
