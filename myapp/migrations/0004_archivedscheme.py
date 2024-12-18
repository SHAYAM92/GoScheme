# Generated by Django 5.0.6 on 2024-06-04 04:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_edueligibility_choice_alter_scheme_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivedScheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived_date', models.DateTimeField(auto_now_add=True)),
                ('original_scheme', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.scheme')),
            ],
        ),
    ]
