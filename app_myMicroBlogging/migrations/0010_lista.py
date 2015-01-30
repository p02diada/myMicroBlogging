# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_myMicroBlogging', '0009_auto_20150114_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='lista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('listaUsuarios', models.ManyToManyField(to='app_myMicroBlogging.my_user')),
                ('usuario', models.ForeignKey(related_name='identificador', to='app_myMicroBlogging.my_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
