# Generated by Django 4.1.4 on 2022-12-28 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_currency_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='order_location',
            field=models.CharField(max_length=500, null=True),
        ),
    ]