from rest_framework.serializers import ModelSerializer
from . import models

class PlayerSerializer(ModelSerializer):
  class Meta:
    model = models.Player
    fields = '__all__'

class TeamSerializer(ModelSerializer):
  players = PlayerSerializer(many=True)

  class Meta:
    model = models.Team
    fields = '__all__'
    extra_fields = ['players']

class MatchSerializer(ModelSerializer):
  class Meta:
    model = models.Match
    fields = '__all__'