# Generated by Django 4.0.3 on 2022-04-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='status',
            field=models.CharField(choices=[('ONGOING', 'Ongoing'), ('RETURNED', 'Returned'), ('OVERDUE', 'Overdue')], default='ONGOING', max_length=8),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('APPROVED', 'Approved'), ('DECLINED', 'Declined'), ('PENDING', 'Pending')], default='PENDING', max_length=8),
        ),
    ]
