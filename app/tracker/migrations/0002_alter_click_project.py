# Generated by Django 5.1.4 on 2024-12-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='project',
            field=models.SlugField(default='default', verbose_name='Проект'),
            preserve_default=False,
        ),
    ]
