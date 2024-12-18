# Generated by Django 5.0.6 on 2024-06-03 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_casteeligibility_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edueligibility',
            name='choice',
            field=models.CharField(choices=[('SSLC', 'SSLC'), ('HSC', 'HSC'), ('DIPLOMA', 'Diploma'), ('PROFESSIONAL', 'Professional'), ('ARTS', 'Arts'), ('P.G', 'P.G'), ('PH.D', 'Ph.D')], max_length=20),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='gender',
            field=models.CharField(choices=[('BOTH', 'BOTH'), ('FEMALE', 'FEMALE'), ('MALE', 'MALE')], max_length=20),
        ),
    ]
