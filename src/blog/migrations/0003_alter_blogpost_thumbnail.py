# Generated by Django 4.2.1 on 2023-05-23 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='blog'),
        ),
    ]
