# Generated by Django 4.0.4 on 2022-06-09 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maker', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
            ],
        ),
    ]
