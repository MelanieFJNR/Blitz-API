# Generated by Django 2.0.8 on 2019-01-15 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_historicalrefund_refund'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='store.Coupon', verbose_name='Applied coupon'),
        ),
    ]
