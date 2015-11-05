# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre_name', models.CharField(max_length=25, choices=[(b'Adventure', b'Adventure'), (b'Family', b'Family'), (b'Fantasy', b'Fantasy'), (b'Musical', b'Musical'), (b'Sci-Fi', b'Sci-Fi'), (b'Drama', b'Drama'), (b'War', b'War'), (b'Animation', b'Animation'), (b'Short', b'Short'), (b'Western', b'Western'), (b'Action', b'Action'), (b'Biography', b'Biography')])),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('popularity', models.DecimalField(max_digits=3, decimal_places=1)),
                ('director', models.CharField(max_length=100)),
                ('imdb_score', models.DecimalField(max_digits=3, decimal_places=1)),
                ('movie_name', models.CharField(max_length=100)),
                ('genre', models.ForeignKey(related_name='genres', to='movie_api.Genre')),
            ],
        ),
    ]
