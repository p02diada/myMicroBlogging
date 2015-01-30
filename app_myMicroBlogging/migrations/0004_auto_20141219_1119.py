# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_myMicroBlogging', '0003_auto_20141218_2301'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='micro_blog',
            new_name='micro_post',
        ),
    ]
