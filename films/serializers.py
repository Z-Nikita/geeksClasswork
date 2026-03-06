from rest_framework import serializers
from .models import Film, Director, Genre


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id fio'.split()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class FilmListSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)
    # genres = GenreSerializer(many=True)
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Film
        fields = 'id title text rating created director genres reviews'.split()
        depth = 1

    def get_genres(self, film):
        return film.genre_names()[0:2]
