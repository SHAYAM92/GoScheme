# Generated by Django 5.0.6 on 2024-06-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casteeligibility',
            name='choice',
            field=models.CharField(choices=[('FOR_ALL_CASTE', 'FOR_ALL_CASTE'), ('MBC', 'MBC'), ('BC', 'BC'), ('OC', 'OC'), ('SC', 'SC'), ('ST', 'ST')], max_length=20, unique=True),
        ),
    ]
