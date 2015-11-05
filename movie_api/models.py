"""
The Movie and Genre are two basic relational models here with Many-to-Many relationship between them.
"""
from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    """
    Genre model
    """
    genre_name = models.CharField(max_length = 25)

    def __unicode__(self):
        return u'%s' % (self.genre_name)

class Movie(models.Model):
    """
    Movie model
    """
    movie_name = models.CharField(max_length = 100)
    director = models.CharField(max_length = 100)

    #genres represent the many-to-many relationship with Genre model 
    genres = models.ManyToManyField(Genre, related_name = 'movies')
    popularity = models.DecimalField(max_digits = 3, decimal_places = 1)
    imdb_score = models.DecimalField(max_digits=3, decimal_places = 1)

    class Meta:
        unique_together = ('movie_name', 'director') #unique key

    def __unicode__(self):
        return u'%s' % (self.movie_name)

class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name='comments')
    comment = models.CharField(max_length = 200)
    owner = models.ForeignKey(User, related_name='comments')

    class Meta:
        unique_together = ('movie', 'owner') #unique key

    def __unicode__(self):
        return u'%s' % (self.comment)




