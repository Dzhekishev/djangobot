# Generated by Django 4.1.2 on 2024-12-26 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0004_phrases_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
            ],
        ),
    ]