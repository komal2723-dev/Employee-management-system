# Generated by Django 5.1.5 on 2025-01-29 14:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
