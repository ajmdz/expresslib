# Generated by Django 4.0.3 on 2022-04-01 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_isbn13'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn13',
            field=models.CharField(max_length=13),
        ),
    ]