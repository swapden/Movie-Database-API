"""
Views and Filters. 
"""
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

#Using the django url filter module for filtering/ Serach 
from url_filter.filtersets import ModelFilterSet 
from movie_api.models import Movie, Genre, Comment
from movie_api.serializers import *
from movie_api.permissions import IsAdminOrReadOnly, IsAdminOrIsOwner, IsOwnerOrReadOnly

#API Root 
@api_view(('GET',))
def api_root(request, format=None):
    """
    Welcome to Movie Database API.

    This Movie Database API will allow you to search from list of Movies.
    You can serach the movies based on movies name(Full text serach). You can search movies based on genres or by director.
    You can as well search based on the popularity and IMDB score.
    Hyperlinks are provided to better naviate through API.
    You can add your comments / reviews about movies by signing up to API.

    Admin/Staff users can manage the backend tasks like updating new movies or genres.

    This Restfull Movie Database API is build using Django Rest Framework. django-url-filter is used for providing the filtering of data or
    search into the data.
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'movies': reverse('movie-list', request=request, format=format),
        'genres': reverse('genre-list', request=request, format=format),
        'commets' : reverse('comment-list', request=request, format=format),
        'signup' : reverse('user-create', request=request, format=format),
    })


#************************************* Filters *************************************

class UserFilterSet(ModelFilterSet):
    """
    Model filter for User model
    """
    class Meta(object):
        model = User

class MovieFilterSet(ModelFilterSet):
    """
    Model filter for Movie model
    """
    class Meta(object):
        model = Movie

class GenreFilterSet(ModelFilterSet):
    """
    Model filter for Genre model
    """
    class Meta(object):
        model = Genre

class CommetFilterSet(ModelFilterSet):
    """
    Model filter for Comment model
    """
    class Meta(object):
        model = Comment


#************************************* Views *************************************
class UserCreate(generics.CreateAPIView):
    """
    Users of the Movie API can signup using this view.
    All the users have access on this view; so that any new user can signup to API. 
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

class GenreCreate(generics.CreateAPIView):
    """
    View to add new movies.
    Only Admin/Staff users have access to this view. 
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = GenreSerializer


class MovieCreate(generics.CreateAPIView):
    """
    View to add new genres.
    Only Admin/Staff users have access to this view. 
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = MovieSerializer


class UserList(generics.ListAPIView):
    """
    List all the registed users.
    Only Admin/Staff user can see this view.
    """
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserListSerializer  
    filter_class = UserFilterSet

class MovieList(generics.ListAPIView):
    """
    User can list all the existing Movies and search based on movie name, director, IMDB score etc.
    All users have access to this view.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_class = MovieFilterSet

class GenreList(generics.ListAPIView):
    """
    User can list all the existing Genres and search based on genre names.
    All users have access to this view.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
    filter_class = GenreFilterSet

class CommentList(generics.ListCreateAPIView):
    """
    This is the list of commets added by the registed users on movies.
    Authenticated user can add comments on movies. One user can add only one comment per movies.
    User can delete his comments.
    Admin/Staff cannot add comments.
    """
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_class = CommetFilterSet

    #Associate user/owner with comment
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Authenticated user can see only his/her details or update the details. User can delete his entry.
    Admin/ Staff have all accesses.
    """
    permission_classes = (IsAdminOrIsOwner,)
    queryset = User.objects.all()
    serializer_class = UserSerializer   

class MovieDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    All the users can see the particular movie details with this view.
    Admin/Staff can edit or delete the movie entry.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class GenreDetails(generics.RetrieveDestroyAPIView):
    """
    All the users can see the particular genres details with this view.
    Admin/Staff can delete the genres entry; update is not provided itentionally.
    """
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class CommentDetails(generics.RetrieveDestroyAPIView):
    """
    Authenticated User can see the details of his/her comments. They can delete their comments. Updates are not allowed.
    Admin/Staff can see the comments details and can delete as well.
    """
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
        