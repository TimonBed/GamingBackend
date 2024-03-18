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
    developer = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Reference(models.Model):
    name = models.CharField(max_length=200)
    game = models.ForeignKey(
        Game, related_name='references', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Image(Content):
    image_file = models.ImageField(upload_to='images', blank=True, null=True)
    reference_image = models.ForeignKey(
        Reference, related_name='image_contents', on_delete=models.CASCADE)


class Video(Content):
    video_link = models.URLField(blank=True, null=True)
    reference_video = models.ForeignKey(
        Reference, related_name='video_contents', on_delete=models.CASCADE)
