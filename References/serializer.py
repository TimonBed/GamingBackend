from .models import Game, GameCategory, Reference, Content, Image, Video
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):

    games = serializers.StringRelatedField(many=True)

    class Meta:
        model = GameCategory
        fields = ('id', 'name', 'games')


class GameSerializer(serializers.HyperlinkedModelSerializer):

    game_category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Game
        fields = ('id', 'game_category', 'name', 'release_date', 'developer')


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = ('id', 'title')


class ImageSerializer(ContentSerializer):
    class Meta(ContentSerializer.Meta):
        model = Image
        fields = ContentSerializer.Meta.fields + \
            ('image_file', 'reference_image',)


class VideoSerializer(ContentSerializer):
    class Meta(ContentSerializer.Meta):
        model = Video
        fields = ContentSerializer.Meta.fields + \
            ('video_link', 'reference_video',)


class ReferenceListSerializer(serializers.ModelSerializer):
    game = serializers.SlugRelatedField(
        queryset=Game.objects.all(), slug_field='name')

    class Meta:
        model = Reference
        fields = ('id', 'name', 'game')


class ReferenceDetailSerializer(serializers.ModelSerializer):
    game = serializers.SlugRelatedField(
        queryset=Game.objects.all(), slug_field='name')
    image_contents = ImageSerializer(many=True, read_only=True)
    video_contents = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Reference
        fields = ('id', 'name', 'game', 'image_contents', 'video_contents')
