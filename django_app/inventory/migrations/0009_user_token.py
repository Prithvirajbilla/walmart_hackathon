# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_predictions_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default=datetime.datetime(2015, 10, 18, 16, 7, 56, 490154, tzinfo=utc), max_length=256),
            preserve_default=False,
        ),
    ]
