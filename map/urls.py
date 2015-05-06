from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^$', 'map.views.map_view'),
                       )
