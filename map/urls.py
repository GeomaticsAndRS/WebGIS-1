from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', 'map.views.map_view'),
                       url(r'^static_geojson$', 'map.views.static_geojson'),
                       )
