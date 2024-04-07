import os
import PIL.Image
from django.db import models
from django.core.files.storage import default_storage
from django.forms import ValidationError
from django.core.validators import FileExtensionValidator
from PIL import Image as PILImage


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
    name = models.CharField(max_length=200, blank=True, null=True)
    game = models.ForeignKey(
        Game, related_name='references', on_delete=models.CASCADE, blank=True, null=True)
    preview_image = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        for image in self.image_contents.all():
            image.delete()
        super().delete(*args, **kwargs)


class Content(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Image(Content):
    image_file = models.ImageField(upload_to='images', blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'webp'])])
    reference_image = models.ForeignKey(
        Reference, related_name='image_contents', on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        if self.image_file:
            image_path = self.image_file.name
            default_storage.delete(image_path)
        super().delete(*args, **kwargs)

    # convert to webp before saving
    def save(self, *args, **kwargs):
        if self.image_file:
            image = PILImage.open(self.image_file)
            webp_image_path = os.path.splitext(
                self.image_file.name)[0] + '.webp'
            webp_image = image.convert('RGB').save(webp_image_path, 'WEBP')
            with open(webp_image_path, 'rb') as f:
                self.image_file.save(webp_image_path, f, save=False)


class Video(Content):
    video_link = models.URLField(blank=True, null=True)
    reference_video = models.ForeignKey(
        Reference, related_name='video_contents', on_delete=models.CASCADE)
