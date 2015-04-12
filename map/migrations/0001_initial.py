# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField()),
                ('width', models.IntegerField()),
                ('precision', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, null=True, max_length=255)),
                ('attribute', models.ForeignKey(to='map.Attribute')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('geom_point', django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326, null=True)),
                ('geom_multipoint', django.contrib.gis.db.models.fields.MultiPointField(blank=True, srid=4326, null=True)),
                ('geom_multilineString', django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, srid=4326, null=True)),
                ('geom_multipolygon', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, srid=4326, null=True)),
                ('geom_geometrycollection', django.contrib.gis.db.models.fields.GeometryCollectionField(blank=True, srid=4326, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('layername', models.CharField(max_length=255)),
                ('srs_wkt', models.CharField(max_length=255)),
                ('geom_type', models.CharField(max_length=50)),
                ('encoding', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='feature',
            name='layer',
            field=models.ForeignKey(to='map.Layer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='feature',
            field=models.ForeignKey(to='map.Feature'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attribute',
            name='layer',
            field=models.ForeignKey(to='map.Layer'),
            preserve_default=True,
        ),
    ]
