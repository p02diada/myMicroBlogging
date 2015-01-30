# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_myMicroBlogging', '0007_favorito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorito',
            name='usuarios',
            field=models.ForeignKey(blank=True, to='app_myMicroBlogging.my_user', null=True),
            preserve_default=True,
        ),
    ]
