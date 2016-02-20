# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerandi_app', '0009_stock_logo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stock_innovation',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock_return',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock_risk',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='stock_sustainability',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='user_name',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
