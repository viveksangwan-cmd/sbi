# Generated by Django 3.0 on 2020-05-13 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20200513_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passbook',
            fields=[
                ('unique_no', models.OneToOneField(default=-1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('transaction_type', models.CharField(default='', max_length=50)),
                ('amount_transfered_to', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('Initial_amount', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('Final_amount', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
