from django.contrib.gis.db import models


class Layer(models.Model):
    layername = models.CharField(max_length=255)
    srs_wkt = models.CharField(max_length=255)
    geom_type = models.CharField(max_length=50)
    encoding = models.CharField(max_length=20)

    def __str__(self):
        return self.layername


class Attribute(models.Model):
    layer = models.ForeignKey(Layer)
    name = models.CharField(max_length=255)
    type = models.IntegerField()
    width = models.IntegerField()
    precision = models.IntegerField()

    def __str__(self):
        return self.name


class Feature(models.Model):
    layer = models.ForeignKey(Layer)
    geom_point = models.PointField(srid=4326, blank=True, null=True)
    geom_multipoint = models.MultiPointField(srid=4326, blank=True, null=True)
    geom_multilineString = models.MultiLineStringField(srid=4326, blank=True, null=True)
    geom_multipolygon = models.MultiPolygonField(srid=4326, blank=True, null=True)
    geom_geometrycollection = models.GeometryCollectionField(srid=4326, blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return self.layer.layername


class AttributeValue(models.Model):
    feature = models.ForeignKey(Feature)
    attribute = models.ForeignKey(Attribute)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.value