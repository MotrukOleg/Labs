from django.contrib.auth.models import User
from rest_framework import serializers
from .models import club, player, match_info, stadium, assist, player_stats


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = club
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = player
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = match_info
        fields = '__all__'

class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = stadium
        fields = '__all__'

class PlayerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = player_stats
        fields = '__all__'

class AssistSerializer(serializers.ModelSerializer):
    class Meta:
        model = assist
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

