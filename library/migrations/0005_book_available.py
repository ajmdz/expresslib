# Generated by Django 4.0.3 on 2022-04-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_book_isbn13'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]