from django.contrib.auth.models import User

from rest_framework import generics, renderers, permissions, status
from rest_framework.response import Response

from .serializers import UserSerializer

# Create your views here.


class CreateUser(generics.GenericAPIView):

    """Creates BNC users for API call from BNC CRM system"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    renderer_classes = (renderers.JSONRenderer,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        error_response = []
        user_objects = []
        return Response({"status": 1})