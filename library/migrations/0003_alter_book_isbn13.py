# Generated by Django 4.0.3 on 2022-04-01 05:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_isbn13'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn13',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999999)]),
        ),
    ]
