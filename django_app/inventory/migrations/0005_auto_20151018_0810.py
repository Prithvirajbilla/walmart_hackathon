# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20151018_0416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasehistory',
            old_name='pruchase_time',
            new_name='purchase_time',
        ),
    ]
