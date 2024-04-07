from .models import GameCategory, Game, Reference, Content, Image, Video
from .serializer import GameCategorySerializer, GameSerializer, ContentSerializer, ImageSerializer, VideoSerializer, ReferenceListSerializer, ReferenceDetailSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
import django_filters


class ReferenceFilter(FilterSet):
    game__name = django_filters.CharFilter(
        field_name='game__name', lookup_expr='icontains')
    game__game_category__name = django_filters.CharFilter(
        field_name='game__game_category__name', lookup_expr='icontains')
    game__release_date = django_filters.DateFilter(
        field_name='game__release_date')
    game__developer = django_filters.CharFilter(
        field_name='game__developer', lookup_expr='icontains')

    class Meta:
        model = Reference
        fields = ['game__name', 'game__game_category__name',
                  'game__release_date', 'game__developer']


class GameCategoryViewSet(viewsets.ModelViewSet):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    permission_classes = [AllowAny]


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [AllowAny]
    lookup_field = 'name'

    # @method_decorator(cache_page(60))
    # def dispatch(cls, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReferenceFilter

    # @method_decorator(cache_page(60))
    # def dispatch(cls, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'list':
            return ReferenceListSerializer
        else:
            return ReferenceDetailSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
