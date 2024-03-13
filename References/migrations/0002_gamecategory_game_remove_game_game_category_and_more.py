# Generated by Django 5.0.2 on 2024-02-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('References', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamecategory',
            name='game',
            field=models.ManyToManyField(related_name='game_categories', to='References.game'),
        ),
        migrations.RemoveField(
            model_name='game',
            name='game_category',
        ),
        migrations.AddField(
            model_name='game',
            name='game_category',
            field=models.ManyToManyField(blank=True, null=True, related_name='games', to='References.gamecategory'),
        ),
    ]
