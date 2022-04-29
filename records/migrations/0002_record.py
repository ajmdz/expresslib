# Generated by Django 4.0.3 on 2022-04-28 05:48

from django.db import migrations, models
import django.db.models.deletion
import records.models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(default=records.models.Record.get_returnDate)),
                ('status', models.CharField(choices=[('ongoing', 'Ongoing'), ('returned', 'Returned'), ('overdue', 'Overdue')], default='ongoing', max_length=8)),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.request')),
            ],
        ),
    ]