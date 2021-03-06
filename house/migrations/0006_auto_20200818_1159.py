# Generated by Django 3.1 on 2020-08-18 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_auto_20200818_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentbill',
            name='amount_paid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='currentbill',
            name='balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='currentbill',
            name='bill_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='currentbill',
            name='carry_balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='currentbill',
            name='month_year',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='currentbill',
            name='paid_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='currentbill',
            name='teneant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='house.teneant'),
        ),
    ]
