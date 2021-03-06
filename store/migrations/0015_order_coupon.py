# Generated by Django 2.0.8 on 2019-01-08 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_optional_applicable_anything'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorder',
            name='coupon',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='store.Coupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='store.Coupon', verbose_name='Applied coupon'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='historicalcoupon',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Value'),
        ),
    ]
