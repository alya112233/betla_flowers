# Generated by Django 5.2.1 on 2025-06-14 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='image',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
