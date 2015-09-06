from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^district/(?P<district_id>[0-9]+)/$', views.district_view, name='distric_view'),
    url(r'^commission/(?P<commission_id>[0-9]+)/$', views.commision_view, name='commission_view'),
    #url(r'^api/)
]
