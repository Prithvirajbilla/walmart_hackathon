# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_predictions_generated_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictions',
            name='generated_time',
        ),
    ]
