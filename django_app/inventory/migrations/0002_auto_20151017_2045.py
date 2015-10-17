# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predictions',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='purchasehistory',
            old_name='sku_id',
            new_name='sku',
        ),
        migrations.RenameField(
            model_name='purchasehistory',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='sku',
            old_name='product_id',
            new_name='product',
        ),
    ]
