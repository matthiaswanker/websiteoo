# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerandi_app', '0008_auto_20151117_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='logo_url',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
