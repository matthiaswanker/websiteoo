# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cerandi_app', '0013_auto_20151118_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stock_risk_text',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
