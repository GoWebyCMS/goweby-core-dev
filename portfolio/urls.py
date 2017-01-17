from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.portfolio_list),
    url(r'^(?P<pk>[0-9]+)/$', views.portfolio_details),
    # url(r'^about/$', views.about, name='about'),
]
