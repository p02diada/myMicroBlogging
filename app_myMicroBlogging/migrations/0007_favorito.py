# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_myMicroBlogging', '0006_auto_20150111_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='favorito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('micro_post', models.OneToOneField(to='app_myMicroBlogging.micro_post')),
                ('usuarios', models.ForeignKey(to='app_myMicroBlogging.my_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
