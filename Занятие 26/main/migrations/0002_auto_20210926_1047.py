# Generated by Django 3.2.7 on 2021-09-26 10:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата отправки'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
    ]
