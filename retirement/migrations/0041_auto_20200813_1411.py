# Generated by Django 2.2.12 on 2020-08-13 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retirement', '0040_auto_20200724_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalretreattype',
            name='average_duration_in_minute',
            field=models.PositiveIntegerField(default=1, verbose_name='Average duration in minute'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalretreattype',
            name='description',
            field=models.TextField(default='placeholder', verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='retreattype',
            name='average_duration_in_minute',
            field=models.PositiveIntegerField(default=1, verbose_name='Average duration in minute'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='retreattype',
            name='description',
            field=models.TextField(default='placeholder', verbose_name='Description'),
            preserve_default=False,
        ),
    ]
