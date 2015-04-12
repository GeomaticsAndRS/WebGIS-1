from django.contrib import admin
from .models import Attribute, Feature, Layer, AttributeValue

# Register your models here.
admin.site.register(Attribute)
admin.site.register(Feature)
admin.site.register(Layer)
admin.site.register(AttributeValue)
