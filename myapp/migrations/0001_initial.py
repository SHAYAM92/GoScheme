# Generated by Django 5.0.6 on 2024-06-03 07:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CasteEligibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('MBC', 'MBC'), ('BC', 'BC'), ('OC', 'OC'), ('SC', 'SC'), ('ST', 'ST')], max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EduEligibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('SSLC', 'SSLC'), ('HSC', 'HSC'), ('DIPLOMA', 'Diploma'), ('PROFESSIONAL', 'Professional'), ('ARTS', 'Arts'), ('P.G', 'P.G'), ('PH.D', 'Ph.D')], max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('gender', models.CharField(choices=[('BOTH', 'BOTH'), ('FEMALE', 'FEMALE'), ('MALE', 'MALE')], max_length=20, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('link', models.URLField()),
                ('procedure_to_apply', models.TextField()),
                ('edu_eligibility', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.edueligibility')),
            ],
        ),
        migrations.CreateModel(
            name='SchemeCasteMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('caste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.casteeligibility')),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.scheme')),
            ],
            options={
                'unique_together': {('scheme', 'caste')},
            },
        ),
    ]