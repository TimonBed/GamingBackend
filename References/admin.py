from django.contrib import admin
from .models import GameCategory, Game, Reference, Content, Image, Video

admin.site.register(GameCategory)
admin.site.register(Reference)
admin.site.register(Game)
admin.site.register(Image)
admin.site.register(Video)
