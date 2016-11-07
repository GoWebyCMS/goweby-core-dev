from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^portfolio_home/$', views.home_page),
    url(r'^portfolio_home/portfolio_list/$', views.portfolio_list),
    url(r'^portfolio_home/(?P<pk>[0-9]+)/$', views.portfolio_details),
    # url(r'^about/$', views.about, name='about'),
]
