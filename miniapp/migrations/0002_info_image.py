# Generated by Django 4.1.2 on 2024-12-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
