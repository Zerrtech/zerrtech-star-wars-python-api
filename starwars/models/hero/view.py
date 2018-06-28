from rest_framework import viewsets, mixins
from starwars.models.hero.serializer import HeroSerializer
from starwars.models.hero.hero import Hero
from starwars.authentication.Auth0 import Auth0Authentication

class HeroViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):

    authentication_classes = (Auth0Authentication,)
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
