# Generated by Django 2.0.5 on 2020-12-16 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=30)),
                ('cust_details', models.TextField(max_length=40)),
            ],
        ),
    ]
