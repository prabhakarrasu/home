# Generated by Django 3.1 on 2020-08-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0006_auto_20200818_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='add_maintenance_amt',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='amount_paid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='maintenance_amt',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='month_year',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='paid_date',
            field=models.DateTimeField(null=True),
        ),
    ]
