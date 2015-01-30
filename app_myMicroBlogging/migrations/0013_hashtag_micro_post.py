# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_myMicroBlogging', '0012_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='micro_post',
            field=models.ManyToManyField(to='app_myMicroBlogging.micro_post'),
            preserve_default=True,
        ),
    ]
