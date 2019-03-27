# Generated by Django 2.0.8 on 2019-03-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retirement', '0007_reservations_refundable'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalreservation',
            name='exchangeable',
            field=models.BooleanField(default=True, verbose_name='Exchangeable'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='exchangeable',
            field=models.BooleanField(default=True, verbose_name='Exchangeable'),
        ),
    ]