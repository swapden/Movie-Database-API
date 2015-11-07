from django.conf.urls import url, include
from movie_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^movies/$', views.MovieList.as_view(), name = 'movie-list'),
    url(r'^movies/add$', views.MovieCreate.as_view(), name = 'movie-create'),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.MovieDetails.as_view(), name = 'movie-detail'),
    url(r'^genres/$', views.GenreList.as_view(), name = 'genre-list'),
    url(r'^genres/add$', views.GenreCreate.as_view(), name = 'genre-create'),
    url(r'^genres/(?P<pk>[0-9]+)/$', views.GenreDetails.as_view(), name = 'genre-detail'),
    url(r'^commets/$', views.CommentList.as_view(), name = 'comment-list'),
    url(r'^commets/(?P<pk>[0-9]+)/$', views.CommentDetails.as_view(), name = 'comment-detail'),
    url(r'^users/$', views.UserList.as_view(), name = 'user-list'),
    url(r'^signup$', views.UserCreate.as_view(), name = 'user-create'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetails.as_view(), name = 'user-detail'), 
]

#URL can be suffixed with the format to get the response in required format
urlpatterns = format_suffix_patterns(urlpatterns)

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

