# Generated by Django 4.1.3 on 2022-11-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_currency_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]