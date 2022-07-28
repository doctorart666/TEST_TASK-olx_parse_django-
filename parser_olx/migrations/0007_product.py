# Generated by Django 4.0.6 on 2022-07-27 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parser_olx', '0006_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_to_product', models.CharField(max_length=255, verbose_name='Посилання на сторінку')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Назва')),
                ('locacion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Локація')),
                ('date_of_creating', models.CharField(blank=True, max_length=100, null=True, verbose_name='Дата створення')),
                ('photo_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Посилання на фото')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Конвертовані дані')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kategory_product', to='parser_olx.category', verbose_name="Пов'язана категорія")),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
    ]
