# Generated by Django 4.0.4 on 2022-05-26 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customadmin_customer_mechanic_tamanager'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TAmanager',
            new_name='TRmanager',
        ),
    ]
