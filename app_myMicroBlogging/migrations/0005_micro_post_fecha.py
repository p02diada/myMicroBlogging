# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_myMicroBlogging', '0004_auto_20141219_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='micro_post',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 1, 11, 19, 50, 46, 82135, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
