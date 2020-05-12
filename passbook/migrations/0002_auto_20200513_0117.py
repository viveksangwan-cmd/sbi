# Generated by Django 3.0 on 2020-05-12 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('passbook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passbook',
            name='id',
        ),
        migrations.AddField(
            model_name='passbook',
            name='Final_amount',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='passbook',
            name='Initial_amount',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='passbook',
            name='amount_transfered_to',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='passbook',
            name='transaction_type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='passbook',
            name='unique_no',
            field=models.OneToOneField(default=-1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
