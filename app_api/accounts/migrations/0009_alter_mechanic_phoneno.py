# Generated by Django 4.0.4 on 2022-05-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customer_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanic',
            name='phoneno',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
