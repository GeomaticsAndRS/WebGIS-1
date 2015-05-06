from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^$', 'map.views.map_view'),
                       url(r'^static_geojson$', 'map.views.static_geojson'),
                       )
