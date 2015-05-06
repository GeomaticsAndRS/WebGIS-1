from django.shortcuts import render_to_response
from .models import Points
from django.core.serializers import serialize
from django.http import HttpResponse

def map_view(request):
    return render_to_response('index.html')


def static_geojson(request):
    return HttpResponse(serialize('geojson', Points.objects.all()), content_type='application/json')
