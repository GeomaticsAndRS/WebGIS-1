from django.contrib.gis.db import models


class PointLayer(models.Model):
    layer_name = models.CharField(max_length=255)

    def __str__(self):
        return self.layer_name


class Attribute(models.Model):
    layer = models.ForeignKey(PointLayer)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Points(models.Model):
    layer = models.ForeignKey(PointLayer)
    geom_point = models.PointField(srid=4326, blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return self.layer.layer_name


class AttributeValue(models.Model):
    point = models.ForeignKey(Points)
    attribute = models.ForeignKey(Attribute)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.attribute.name