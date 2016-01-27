from rest_framework import serializers

from .models import Movie, Genre, Director


class DirectorSerializer(serializers.ModelSerializer):

	"""
		Serializing director model
	"""

	class Meta:
		model = Director


class GenreSerializer(serializers.ModelSerializer):

	"""
		Serializing genre model
	"""

	class Meta:
		model = Genre


class MovieSerializer(serializers.ModelSerializer):

	"""
		Serializing movie model
	"""

	director = DirectorSerializer()
	genre = GenreSerializer()

	class Meta:
		model = Movie
		fields = ('name', 'imdb_score', 'popularity', 'director', 'genre')

	# def create(self, validated_data):
	# 	director_name = validated_data['director']
	# 	director = Director.objects.get_or_create(name=director_name)
	# 	serialized_director = DirectorSerializer(director[0])
	# 	genres = validated_data['genre']
	# 	genre_list = []
	# 	serialized_genre = GenreSerializer(genre_list, many=True)
	# 	validated_data['director'] = director[0]
	# 	del validated_data['genre']
	# 	movie_obj = Movie.objects.create(**validated_data)
	# 	for genre_name in genres:
	# 		genre = Genre.objects.get_or_create(name=genre_name)
	# 		movie_obj.genre.add(genre[0])
	# 	print movie_obj
	# 	return movie_obj
