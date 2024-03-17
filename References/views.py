from .models import GameCategory, Game, Reference, Content, Image, Video
from .serializer import GameCategorySerializer, GameSerializer, ReferenceSerializer, ContentSerializer, ImageSerializer, VideoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny


class GameCategoryViewSet(viewsets.ModelViewSet):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'name'


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = [AllowAny]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
