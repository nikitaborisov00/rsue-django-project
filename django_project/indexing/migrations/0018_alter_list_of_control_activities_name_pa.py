# Generated by Django 4.0.4 on 2022-06-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexing', '0017_alter_list_of_control_activities_name_pa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_of_control_activities',
            name='name_pa',
            field=models.CharField(choices=[('Экзамен', 'Экзамен'), ('Зачёт', 'Зачёт')], default='exam', max_length=20, verbose_name='Вид ПА'),
        ),
    ]
