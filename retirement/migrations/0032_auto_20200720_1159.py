# Generated by Django 2.2.12 on 2020-07-20 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retirement', '0031_auto_20200720_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalretreat',
            old_name='type_new',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='retreat',
            old_name='type_new',
            new_name='type',
        ),
    ]