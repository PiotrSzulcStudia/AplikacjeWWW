from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^vote2/', include('vote2.urls')),
    url(r'^vote3/', include('vote3.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'selector.views.index', name='home_index'),
)
