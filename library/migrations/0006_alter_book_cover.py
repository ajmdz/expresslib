# Generated by Django 4.0.3 on 2022-04-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_book_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]