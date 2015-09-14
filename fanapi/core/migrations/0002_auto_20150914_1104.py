# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='height',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='width',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='terrain',
            name='material',
            field=models.IntegerField(choices=[(0, b'Field'), (1, b'Grass'), (2, b'Rock'), (3, b'River')]),
        ),
    ]
