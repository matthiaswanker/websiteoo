# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerandi_app', '0010_auto_20151117_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='client',
            field=models.ForeignKey(to='cerandi_app.Client'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='stock',
            field=models.ForeignKey(to='cerandi_app.Stock'),
        ),
    ]
