# Generated by Django 4.0.3 on 2022-04-01 05:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn13',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')]),
        ),
    ]