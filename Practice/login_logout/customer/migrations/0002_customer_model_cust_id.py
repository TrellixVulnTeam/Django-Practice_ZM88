# Generated by Django 2.0.5 on 2020-12-17 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_model',
            name='cust_id',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]