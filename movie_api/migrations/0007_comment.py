# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie_api', '0006_auto_20151104_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=200)),
                ('movie', models.ForeignKey(to='movie_api.Movie')),
                ('owner', models.ForeignKey(related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
