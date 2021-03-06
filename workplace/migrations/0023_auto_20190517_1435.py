# Generated by Django 2.0.8 on 2019-05-17 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workplace', '0022_workplace_volunteers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalperiod',
            name='workplace',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workplace.Workplace', verbose_name='Workplace'),
        ),
        migrations.AlterField(
            model_name='historicalpicture',
            name='workplace',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workplace.Workplace', verbose_name='Workplace'),
        ),
        migrations.AlterField(
            model_name='historicalreservation',
            name='timeslot',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workplace.TimeSlot', verbose_name='Time slot'),
        ),
        migrations.AlterField(
            model_name='historicalreservation',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='historicaltimeslot',
            name='period',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workplace.Period', verbose_name='Period'),
        ),
    ]
