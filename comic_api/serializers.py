from rest_framework import serializers
from .models import Hero, Villain


# Create a serializer for the Hero model
class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')


class VillainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Villain
        fields = ('id', 'name', 'alias')
