from .models import GameCategory, Game, Reference
from .serializer import GameCategorySerializer, GameSerializer, ReferenceSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class GameCategoryViewSet(viewsets.ModelViewSet):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
