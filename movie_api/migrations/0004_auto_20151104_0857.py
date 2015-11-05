# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_api', '0003_auto_20151104_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(unique=True, max_length=25, choices=[(b'Adventure', b'Adventure'), (b'Family', b'Family'), (b'Fantasy', b'Fantasy'), (b'Musical', b'Musical'), (b'Sci-Fi', b'Sci-Fi'), (b'Drama', b'Drama'), (b'War', b'War'), (b'Animation', b'Animation'), (b'Short', b'Short'), (b'Western', b'Western'), (b'Action', b'Action'), (b'Biography', b'Biography')]),
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together=set([('movie_name', 'director')]),
        ),
    ]
