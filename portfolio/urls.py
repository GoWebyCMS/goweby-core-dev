from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.portfolio_list, name='portfolio_list'),
    url(r'^project/(?P<pk>[0-9]+)/$', views.portfolio_detail, name='portfolio_detail'),
    # url(r'^about/$', views.about, name='about'),
]
