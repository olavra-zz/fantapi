# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'100')),
            ],
        ),
        migrations.CreateModel(
            name='Terrain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('material', models.IntegerField(choices=[(0, b'Field'), (1, b'Grass'), (2, b'River'), (3, b'Rock')])),
                ('map', models.ForeignKey(to='core.Map')),
            ],
        ),
    ]
