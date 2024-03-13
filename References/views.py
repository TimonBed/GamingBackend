from .models import GameCategory, Game
from .serializer import GameCategorySerializer, GameSerializer
from rest_framework import viewsets


class GameCategoryViewSet(viewsets.ModelViewSet):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
