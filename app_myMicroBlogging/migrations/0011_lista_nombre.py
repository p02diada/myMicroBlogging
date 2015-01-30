# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_myMicroBlogging', '0010_lista'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista',
            name='nombre',
            field=models.CharField(default=0, unique=True, max_length=30),
            preserve_default=False,
        ),
    ]
