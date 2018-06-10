from rest_framework import serializers
from .models import Game, Move


class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'game_collation', )

    def create(self, validated_data):
        return Game.objects.create(**validated_data)


class MoveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ('id', 'pos_from', 'pos_to', 'game', )
