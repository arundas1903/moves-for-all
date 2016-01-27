from rest_framework import generics, renderers, permissions, status
from rest_framework.response import Response

from .serializers import MovieSerializer
from .models import Movie, Genre, Director
from app_user.permissions import IsAdminUser


class Movies(generics.GenericAPIView):

    """
        API to create and view users.
        IsAdminUser permission is set for POST as movies can be created 
        by admins only.
    """

    # serializer_class = UserSerializer
    queryset = Movie.objects.all()
    permission_classes = (permissions.IsAuthenticated, 
        IsAdminUser)

    def post(self, request, *args, **kwargs):
        data = request.data
        movie_serializer = MovieSerializer(data=data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response({'status': 1, 'movie': movie_serializer.data})
        return Response({'status': -1, 'errors': movie_serializer.errors})
