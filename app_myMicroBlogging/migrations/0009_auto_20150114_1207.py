# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_myMicroBlogging', '0008_auto_20150114_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorito',
            name='micro_post',
            field=models.ForeignKey(to='app_myMicroBlogging.micro_post'),
            preserve_default=True,
        ),
    ]
