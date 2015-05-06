from django.contrib import admin
from .models import Attribute, PointLayer


class AttributeInline(admin.TabularInline):
    model = Attribute


class LayerAdmin(admin.ModelAdmin):
    inlines = [
        AttributeInline,
        ]


# Register your models here.
admin.site.register(PointLayer, LayerAdmin)
