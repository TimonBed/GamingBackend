from django.contrib import admin
from .models import GameCategory, Game, Reference

admin.site.register(GameCategory)
admin.site.register(Reference)
admin.site.register(Game)
