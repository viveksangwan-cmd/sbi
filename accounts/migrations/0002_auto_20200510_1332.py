# Generated by Django 3.0 on 2020-05-10 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(blank=True, default='2242275342', editable=False, max_length=10, unique=True),
        ),
    ]
