# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20150506_0847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attributevalue',
            old_name='feature',
            new_name='point',
        ),
    ]
