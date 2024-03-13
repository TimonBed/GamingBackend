from .models import Game, GameCategory
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
