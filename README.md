# Movie-Database-API

Movie Database API is simple search API to search the movies from the movies database.

# Here are some features of this API
1. User can list all the movies and genres available. As well the comments put by the users on movies.
2. Users can search the movies based on movie name, director name, genres , IMDB score and popularity.
3. Users can register to api and add the comments on movies.
4. Admin users can add new movies/genres to the database.

# Major libraries used
1. Django Rest Framework (https://github.com/tomchristie/django-rest-framework)
2. Djngo URL Filter (https://github.com/miki725/django-url-filter)


# Usage Examples 
This is the json file containging the movie entry:
```
PRINHYLTPAP0472:~ swapnild$ cat movie.json 
{
  "popularity": 62.0,
  "director": "Michael Curtiz",
  "genres": [
    {"genre_name":"Drama"},
    {"genre_name":"History"}
  ],
  "imdb_score": 6.2,
  "movie_name": "The Egyptian"
}
```

Sending the POST request to add the entry:
````
$ http -a admin:admin POST https://movie-database-api.herokuapp.com/movies/add < movie.json 
HTTP/1.1 201 CREATED
Allow: POST, OPTIONS
Connection: close
Content-Type: application/json
Date: Sat, 07 Nov 2015 13:39:04 GMT
Server: WSGIServer/0.1 Python/2.7.10
Vary: Accept, Cookie
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

{
    "comments": [], 
    "director": "Michael Curtiz", 
    "genres": [
        {
            "genre_name": "History", 
            "url": "https://movie-database-api.herokuapp.com/genres/17/"
        }, 
        {
            "genre_name": "Drama", 
            "url": "https://movie-database-api.herokuapp.com/genres/24/"
        }
    ], 
    "imdb_score": "6.2", 
    "movie_name": "The Egyptian", 
    "popularity": "62.0"
}
```

See the details of added entry:
```
$ http GET https://movie-database-api.herokuapp.com/movies/?movie_name='The Egyptian'
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Connection: close
Content-Type: application/json
Date: Sat, 07 Nov 2015 13:39:23 GMT
Server: WSGIServer/0.1 Python/2.7.10
Vary: Accept, Cookie
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

{
    "count": 1, 
    "next": null, 
    "previous": null, 
    "results": [
        {
            "movie_name": "The Egyptian", 
            "url": "https://movie-database-api.herokuapp.com/movies/153/"
        }
    ]
}


$ http GET https://movie-database-api.herokuapp.com/movies/153/
HTTP/1.1 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Connection: close
Content-Type: application/json
Date: Sat, 07 Nov 2015 13:39:50 GMT
Server: WSGIServer/0.1 Python/2.7.10
Vary: Accept, Cookie
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

{
    "comments": [], 
    "director": "Michael Curtiz", 
    "genres": [
        {
            "genre_name": "History", 
            "url": "https://movie-database-api.herokuapp.com/genres/17/"
        }, 
        {
            "genre_name": "Drama", 
            "url": "https://movie-database-api.herokuapp.com/genres/24/"
        }
    ], 
    "imdb_score": "6.2", 
    "movie_name": "The Egyptian", 
    "popularity": "62.0"
}

```
 





