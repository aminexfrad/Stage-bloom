# Generated by Django 5.0.2 on 2025-07-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='date de modification'),
        ),
    ]
