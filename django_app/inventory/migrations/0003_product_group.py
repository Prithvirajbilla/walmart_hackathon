# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20151017_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.BooleanField(default=False),
        ),
    ]
