# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_api', '0004_auto_20151104_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(unique=True, max_length=25),
        ),
    ]
