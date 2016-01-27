from rest_framework import generics, renderers, permissions, status
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import AppUser

# Create your views here.


class CreateAppUser(generics.GenericAPIView):

    """
        Creates App users for API call
    """

    serializer_class = UserSerializer
    queryset = AppUser.objects.all()
    renderer_classes = (renderers.JSONRenderer,)
    # permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        print request
        print dir(request)
        print request.data
        error_response = []
        user_objects = []
        return Response({"status": 1})