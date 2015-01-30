# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_myMicroBlogging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_user',
            name='seguidos',
            field=models.ManyToManyField(to='app_myMicroBlogging.my_user', blank=True),
            preserve_default=True,
        ),
    ]
