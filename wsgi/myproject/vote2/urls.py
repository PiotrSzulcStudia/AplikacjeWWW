from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^district/(?P<district_id>[0-9]+)/$'),
    #url(r'^commission/(?P<district_id>[0-9]+)/$'),
]
