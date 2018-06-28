from rest_framework import serializers
from starwars.models.hero.hero import Hero

class HeroSerializer(serializers.ModelSerializer):
    affiliations = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Hero
        fields = (
            'id',
            'name',
            'affiliations',
            'power',
            'imageUrl',
            'light',
        )