# Generated by Django 4.2 on 2024-10-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_model_model_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='model_type',
        ),
        migrations.AddField(
            model_name='model',
            name='model_sex',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model',
            name='position_type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
