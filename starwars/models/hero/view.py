from rest_framework import viewsets, mixins
from starwars.models.hero.serializer import HeroSerializer
from starwars.models.hero.hero import Hero
from starwars.authentication.Auth0 import Auth0Authentication
from rest_framework.response import Response
import json

class HeroViewSet(mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):

    authentication_classes = (Auth0Authentication,)
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    def update(self, request, *args, **kwargs):
        # Mock the update so we don't actually modify the database
        return Response(json.loads(request.body))
