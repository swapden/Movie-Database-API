# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_api', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(related_name='comments', to='movie_api.Movie'),
        ),
    ]
