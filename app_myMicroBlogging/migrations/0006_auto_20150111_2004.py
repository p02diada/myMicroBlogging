# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_myMicroBlogging', '0005_micro_post_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='micro_post',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
