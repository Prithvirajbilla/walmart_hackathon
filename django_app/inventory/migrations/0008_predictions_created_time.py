# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_predictions_generated_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictions',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 18, 14, 56, 42, 710170, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
