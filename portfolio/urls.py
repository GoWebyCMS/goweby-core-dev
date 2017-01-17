from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.portfolio_list, name='portfolio_list'),
    url(r'^project/(?P<slug>[\w-]+)/$', views.portfolio_detail, name='portfolio_detail'),
    # url(r'^about/$', views.about, name='about'),
]
