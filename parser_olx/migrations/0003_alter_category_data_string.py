# Generated by Django 4.0.6 on 2022-07-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_olx', '0002_alter_category_data_string'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='data_string',
            field=models.TextField(blank=True, null=True, verbose_name='Конвертовані дані'),
        ),
    ]
