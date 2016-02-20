# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerandi_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisor',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='client',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='stock',
        ),
        migrations.AlterModelOptions(
            name='client',
            options={},
        ),
        migrations.RemoveField(
            model_name='client',
            name='gender',
        ),
        migrations.DeleteModel(
            name='Advisor',
        ),
        migrations.DeleteModel(
            name='Bank',
        ),
        migrations.DeleteModel(
            name='Investment',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
