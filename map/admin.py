from django.contrib import admin
from .models import Attribute, PointLayer, AttributeValue


class AttributeInline(admin.TabularInline):
    model = Attribute


class LayerAdmin(admin.ModelAdmin):
    inlines = [
        AttributeInline,
        ]


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue


class PointsAdmin(admin.ModelAdmin):
    inlines = [
        AttributeValueInline,
    ]


# Register your models here.
admin.site.register(PointLayer, LayerAdmin)
