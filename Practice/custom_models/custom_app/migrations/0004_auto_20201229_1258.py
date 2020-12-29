# Generated by Django 3.1.4 on 2020-12-29 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_app', '0003_auto_20201228_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(null=True, upload_to='user_imgs/'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course',
            field=models.CharField(choices=[('Engineering', (('Software Engineering', 'SE'), ('Computer Engineering', 'CE'), ('Electrical Engineering', 'EE'))), ('Commerce', (('Bachelor of Business Administration', 'BBA'), ('Chartered Accountancy', 'CA'))), ('Medical', (('Neuroscience', 'NS'), ('Bachelor of Medicine, Bachelor of Surgery', 'MBBS')))], max_length=50, unique=True),
        ),
    ]