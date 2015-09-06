# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote2', '0004_auto_20150812_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='timesModificated',
            field=models.IntegerField(default=0),
        ),
    ]
