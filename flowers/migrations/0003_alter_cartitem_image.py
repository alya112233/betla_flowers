# Generated by Django 5.2.1 on 2025-06-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0002_cartitem_description_cartitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
