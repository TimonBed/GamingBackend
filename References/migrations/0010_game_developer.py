# Generated by Django 5.0.3 on 2024-03-18 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('References', '0009_rename_reference_video_image_reference_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
