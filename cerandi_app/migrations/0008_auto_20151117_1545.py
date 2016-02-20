# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerandi_app', '0007_auto_20151117_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisor',
            name='friend_score',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='advisor',
            name='past_performance',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
