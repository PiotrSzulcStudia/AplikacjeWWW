# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commision',
            name='receivedCardsToVote',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='commision',
            name='votersAllowedToVote',
            field=models.IntegerField(default=0),
        ),
    ]
