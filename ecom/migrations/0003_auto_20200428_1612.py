# Generated by Django 3.0.5 on 2020-04-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_auto_20200428_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='amout'),
        ),
    ]
