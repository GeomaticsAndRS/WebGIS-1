from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'WebGIS.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^map/', include('map.urls')),
                       url(r'^$', 'main_page.views.main_page'),
                       )
