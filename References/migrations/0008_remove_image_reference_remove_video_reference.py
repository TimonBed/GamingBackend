# Generated by Django 5.0.3 on 2024-03-17 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('References', '0007_image_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='video',
            name='reference',
        ),
    ]
