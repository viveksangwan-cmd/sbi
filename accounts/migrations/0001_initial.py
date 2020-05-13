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
            name='Account',
            fields=[
                ('unique_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('account_number', models.CharField(blank=True, default='9018598085', editable=False, max_length=10, unique=True)),
                ('balance', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
    ]
