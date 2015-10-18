# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=128)),
                ('predicted_datetime', models.DateTimeField()),
                ('predicted_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, db_index=True)),
                ('category', models.CharField(max_length=128, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_datetime', models.DateTimeField()),
                ('pruchase_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('type_quantity', models.CharField(max_length=10)),
                ('product_id', models.ForeignKey(to='inventory.Product')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=128)),
                ('last_updated', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='sku_id',
            field=models.ForeignKey(to='inventory.Sku'),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='user_id',
            field=models.ForeignKey(to='inventory.User'),
        ),
        migrations.AddField(
            model_name='predictions',
            name='user_id',
            field=models.ForeignKey(to='inventory.User'),
        ),
    ]
