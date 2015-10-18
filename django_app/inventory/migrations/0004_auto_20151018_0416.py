# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_product_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='group',
            new_name='group_by',
        ),
    ]
