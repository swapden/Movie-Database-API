"""
Serializers for models. 
"""
from rest_framework import serializers
from movie_api.models import Movie, Genre, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for User model. User model is from django.contrib.auth.models
    """
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only = True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'comments')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        """
        Overriding the create method of serializers so as to set the password in encrypted format
        """
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password']) #set_password will encrypt the inputted password
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Overriding the update method of serializers so as to set the password in encrypted format
        """
        instance.username = validated_data['username']
        instance.email = validated_data['email']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Genre model
    """
    movies = serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only = True)

    class Meta:
        model = Genre
        fields = ('url', 'genre_name', 'movies')

    def create(self, validated_data):
        """
        Overring the create method of serializers so as to avoid creation of duplicate genres.
        Tried putting the unique key on genre_name but it was causing to failed is_valid()
        """
        genre, created = Genre.objects.get_or_create(**validated_data)
        return genre

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Movie model with nested relationship with GenreSerializer.
    """
    url = serializers.HyperlinkedIdentityField(view_name='movie-detail')
    genres = GenreSerializer(many=True) #Nested serializer 
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only = True)

    class Meta:
        model = Movie
        fields = ('url', 'movie_name', 'director', 'genres', 'popularity', 'imdb_score', 'comments')

    def create(self, validated_data):
        """
        Overring the create method of serializers so as to create the Genre object or create reference to existing Genre objects
        as writable nested serializes are not fully suppored.
        """
        genres_data = validated_data.pop('genres')
        movie = Movie.objects.create(**validated_data)

        for genre in genres_data:
            genre, created = Genre.objects.get_or_create(genre_name = genre['genre_name'])
            movie.genres.add(genre)

        return movie

    def update(self, instance, validated_data):
        """
        As create method overriding update method to support nested relationship
        """
        genres_data = validated_data.pop('genres')
        instance.popularity = validated_data['popularity']
        instance.director = validated_data['director']
        instance.imdb_score = validated_data['imdb_score']
        instance.movie_name = validated_data['movie_name']

        #Trying to put in simple way. Just deleting the existing relationships and creating new ones.
        instance.genres.clear()
        for genre in genres_data:
            genre, created = Genre.objects.get_or_create(genre_name = genre['genre_name'])
            instance.genres.add(genre)

        return 

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    movie = serializers.PrimaryKeyRelatedField(queryset = Movie.objects.all())

    class Meta:
        model = Comment

