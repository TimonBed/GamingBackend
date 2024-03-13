from django.db import models


class GameCategory(models.Model):
    name = models.CharField(max_length=200)
    game = models.ManyToManyField(
        'Game', related_name='game_categories', blank=True)

    class Meta:
        verbose_name_plural = "Game Categories"

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=200)
    game_category = models.ManyToManyField(
        GameCategory, related_name='games', blank=True)
    release_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
