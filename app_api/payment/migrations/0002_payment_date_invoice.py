# Generated by Django 4.0.4 on 2022-06-13 01:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_rename_user_customadmin_custom_admin_and_more'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_no', models.CharField(max_length=255)),
                ('rate', models.IntegerField()),
                ('amount', models.FloatField()),
                ('picture', models.FileField(blank=True, upload_to='uploads')),
                ('status', models.BooleanField(default=False)),
                ('paid_at', models.DateTimeField(auto_now_add=True)),
                ('mechanic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.mechanic')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.payment')),
            ],
        ),
    ]
