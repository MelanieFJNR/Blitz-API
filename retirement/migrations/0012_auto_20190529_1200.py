# Generated by Django 2.0.8 on 2019-05-29 16:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_historicalmembershipcoupon_membershipcoupon'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('retirement', '0011_auto_20190517_1435'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalRetirement',
            new_name='HistoricalRetreat',
        ),
        migrations.RenameModel(
            old_name='Retirement',
            new_name='Retreat',
        ),
    ]
