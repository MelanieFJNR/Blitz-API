# Generated by Django 2.0.2 on 2018-06-22 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20171230_2347'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
        migrations.RemoveField(
            model_name='address',
            name='state_province',
        ),
        migrations.RemoveField(
            model_name='stateprovince',
            name='country',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='StateProvince',
        ),
    ]
