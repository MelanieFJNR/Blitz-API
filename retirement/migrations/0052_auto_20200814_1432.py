# Generated by Django 2.2.12 on 2020-08-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retirement', '0051_auto_20200814_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalretreattype',
            name='know_more_link',
            field=models.TextField(default='placeholder', verbose_name='Know more link'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='retreattype',
            name='know_more_link',
            field=models.TextField(default='placeholder', verbose_name='Know more link'),
            preserve_default=False,
        ),
    ]