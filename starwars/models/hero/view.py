from rest_framework import viewsets
from starwars.models.hero.serializer import HeroSerializer
from starwars.models.hero.hero import Hero

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
