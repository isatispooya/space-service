# Generated by Django 4.1.13 on 2024-06-20 07:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brokeragetransactions',
            name='Update',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 20, 7, 56, 51, 659442, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='customerremain',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', unique=True),
        ),
    ]