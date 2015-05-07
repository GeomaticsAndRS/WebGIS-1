from django.shortcuts import render_to_response
from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.gdal import SpatialReference, CoordTransform
from .models import Points

WGS_PRJ = SpatialReference(4326)
MERC_PRJ = SpatialReference(3857)
TRANSF = CoordTransform(MERC_PRJ, WGS_PRJ)


def map_view(request):
    return render_to_response('index.html')


def static_geojson(request):
    return HttpResponse(serialize('geojson', Points.objects.all()), content_type='application/json')


def dynamic_geojson(request):
    bbox = request.GET.get('bbox', None)
    if bbox:
        bbox = [float(x) for x in bbox.split(',')]
    else:
        bbox = [-180, -90, 180, 90]  # TODO: calc to 3857
    bbox_dict = {
        'min_x': bbox[0],
        'min_y': bbox[1],
        'max_x': bbox[2],
        'max_y': bbox[3],
        }
    geom = GEOSGeometry(
        'POLYGON (({min_x} {min_y}, {min_x} {max_y}, {max_x} {max_y}, {max_x} {min_y}, {min_x} {min_y}))'.format(
            **bbox_dict
        ))
    geom.srid = 3857
    geom.transform(TRANSF)
    points = Points.objects.filter(geom_point__bboverlaps=geom)
    return HttpResponse(serialize('geojson', points), content_type='application/json')
