# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20151018_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictions',
            name='generated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 18, 14, 55, 3, 323691)),
            preserve_default=False,
        ),
    ]
