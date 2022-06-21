# Generated by Django 4.0.5 on 2022-06-06 15:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('indexing', '0012_alter_group_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='teacher',
            field=models.ManyToManyField(related_name='student_groups', related_query_name='student_groups', to=settings.AUTH_USER_MODEL, verbose_name='Учитель'),
        ),
    ]