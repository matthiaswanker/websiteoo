# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerandi_app', '0012_auto_20151118_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='service_url',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock_innovation_text',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock_sustainability_text',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
