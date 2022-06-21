# Generated by Django 4.0.4 on 2022-06-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexing', '0014_rename_group_studentgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_of_control_activities',
            name='evaluation_criteria_pa',
            field=models.TextField(default=2, verbose_name='Критерии оценивания ПА'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list_of_control_activities',
            name='evaluation_scale_pa',
            field=models.CharField(default=2, max_length=350, verbose_name='Шкала оценивания ПА'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list_of_control_activities',
            name='head_department',
            field=models.CharField(default='', max_length=350, verbose_name='Зав.Кафедрой'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list_of_control_activities',
            name='order_holding_pa',
            field=models.CharField(default='', max_length=350, verbose_name='Порядок проведения ПА'),
            preserve_default=False,
        ),
    ]
