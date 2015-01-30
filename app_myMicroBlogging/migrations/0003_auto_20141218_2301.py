# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_myMicroBlogging', '0002_auto_20141218_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_user',
            name='seguidos',
            field=models.ManyToManyField(to='app_myMicroBlogging.my_user', null=True, blank=True),
            preserve_default=True,
        ),
    ]
