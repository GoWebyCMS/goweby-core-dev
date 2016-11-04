from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^portfolio_home/$', views.home_page),
    url(r'^portfolio_home/portfolio_list/$', views.portfolio_list),
    # url(r'^about/$', views.about, name='about'),
]
