# Generated by Django 3.0.5 on 2020-05-08 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_remove_transaction_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='img_pro',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name_pro',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price_pro',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='address_user',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='firstname_user',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='lastname_user',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='phone_user',
            new_name='phone',
        ),
    ]
