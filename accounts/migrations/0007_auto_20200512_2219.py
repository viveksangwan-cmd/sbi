# Generated by Django 3.0 on 2020-05-12 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200512_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(blank=True, default='9777621560', editable=False, max_length=10, unique=True),
        ),
    ]