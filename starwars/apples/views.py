from rest_framework.views import APIView
from rest_framework.response import Response
from starwars.authentication.Auth0 import Auth0Authentication

class ListApples(APIView):
    """
    View apples
    """
    authentication_classes = (Auth0Authentication,)

    def get(self, request, format=None):
        """
        Return list of apples
        :param request:
        :param format:
        :return:
        """

        apples = ["Fuji", "Granny Smith", "Pink Lady"]
        return Response(apples)