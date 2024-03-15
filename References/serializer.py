from .models import Game, GameCategory, Reference
from rest_framework import serializers


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):

    games = serializers.StringRelatedField(many=True)

    class Meta:
        model = GameCategory
        fields = ('id', 'name', 'games')


class GameSerializer(serializers.HyperlinkedModelSerializer):

    game_category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Game
        fields = ('id', 'game_category', 'name', 'release_date')


class ReferenceSerializer(serializers.HyperlinkedModelSerializer):

    game = serializers.SlugRelatedField(
        queryset=Game.objects.all(), slug_field='name')

    class Meta:
        model = Reference
        fields = ('id', 'name', 'game')
