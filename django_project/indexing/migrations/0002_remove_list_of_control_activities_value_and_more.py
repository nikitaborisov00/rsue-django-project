# Generated by Django 4.0.4 on 2022-04-27 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list_of_control_activities',
            name='value',
        ),
        migrations.AddField(
            model_name='list_of_control_activities_value',
            name='value',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='indexing.list_of_control_activities', verbose_name='Содержание'),
            preserve_default=False,
        ),
    ]