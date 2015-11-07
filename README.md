# Movie-Database-API
Movie Database API is simple search API to search the movies from the movies database.


## Features
1. User can list all the movies and genres available. As well the comments put by the users on movies.
2. Users can search the movies based on movie name, director name, genres , IMDB score and popularity.
3. Users can register to api and add the comments on movies.
4. Admin users can add new movies/genres to the database.

## Major libraries used
1. Django Rest Framework (https://github.com/tomchristie/django-rest-framework)
2. Djngo URL Filter (https://github.com/miki725/django-url-filter)


## Usage Examples 
#### Adding New Movies
This is the json file containging the movie entry
```
$ cat movie.json 
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

Sending the POST request to add the entry
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


#### Getting the details of Movie
Send the GET request usind the movie id
```
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


#### Serching Movies
**Searching based on Movie fields**
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
```


**Full text search**
```
$ http GET https://movie-database-api.herokuapp.com/movies/?movie_name__contains="war"
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Connection: close
Content-Type: application/json
Date: Sat, 07 Nov 2015 14:04:34 GMT
Server: WSGIServer/0.1 Python/2.7.10
Vary: Accept, Cookie
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

{
    "count": 4, 
    "next": null, 
    "previous": null, 
    "results": [
        {
            "movie_name": "Star Wars", 
            "url": "https://movie-database-api.herokuapp.com/movies/1/"
        }, 
        {
            "movie_name": "Snow White and the Seven Dwarfs", 
            "url": "https://movie-database-api.herokuapp.com/movies/8/"
        }, 
        {
            "movie_name": "Star Wars : Episode V - The Empire Strikes Back", 
            "url": "https://movie-database-api.herokuapp.com/movies/28/"
        }, 
        {
            "movie_name": "Star Wars : Episode VI - Return of the Jedi", 
            "url": "https://movie-database-api.herokuapp.com/movies/114/"
        }
    ]
}
```


**Searching based on model relations**
```
$ http GET https://movie-database-api.herokuapp.com/movies/?genres__genre_name="Sci-Fi"
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Connection: close
Content-Type: application/json
Date: Sat, 07 Nov 2015 14:07:28 GMT
Server: WSGIServer/0.1 Python/2.7.10
Vary: Accept, Cookie
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

{
    "count": 29, 
    "next": "https://movie-database-api.herokuapp.com/movies/?genres__genre_name=Sci-Fi&page=2", 
    "previous": null, 
    "results": [
        {
            "movie_name": "Star Wars", 
            "url": "https://movie-database-api.herokuapp.com/movies/1/"
        }, 
        {
            "movie_name": "Metropolis", 
            "url": "https://movie-database-api.herokuapp.com/movies/5/"
        }, 
        {
            "movie_name": "Star Trek", 
            "url": "https://movie-database-api.herokuapp.com/movies/6/"
        }, 
        {
            "movie_name": "2001 : A Space Odyssey", 
            "url": "https://movie-database-api.herokuapp.com/movies/9/"
        }, 
        {
            "movie_name": "The Terminator", 
            "url": "https://movie-database-api.herokuapp.com/movies/25/"
        }
    ]
}
```
```
$ http GET https://movie-database-api.herokuapp.com/movies/?movie_name__contains="Merry"&genres__genre_name="Comedy"
[1] 19655
$ HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Connection: close
Content-Type: application/json
Date: Sat, 07 Nov 2015 14:16:45 GMT
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
            "movie_name": "The Merry Widow", 
            "url": "https://movie-database-api.herokuapp.com/movies/17/"
        }
    ]
}
```


*Note: As the django-url-filter is used, its possible to use all the supported filter by django-url-filter.*


#### Permissions and Authentications
**Only Admin/Staff users have permissions to add new Movies/ Genres**
```
$ http -a James:James123 POST https://movie-database-api.herokuapp.com/movies/add < movie.json 
HTTP/1.1 403 FORBIDDEN
Allow: POST, OPTIONS
Connection: close
Content-Type: application/json
Date: Sat, 07 Nov 2015 13:45:21 GMT
Server: WSGIServer/0.1 Python/2.7.10
Vary: Accept, Cookie
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

{
    "detail": "You do not have permission to perform this action."
}
```


**2. Any User can register to the API**
```
PRINHYLTPAP0472:~ swapnild$ http POST https://movie-database-api.herokuapp.com/signup username="John" password="John123" email="john@gmail.com" first_name="John" last_name="Hitchcock"
HTTP/1.1 201 CREATED
Allow: POST, OPTIONS
Connection: close
Content-Type: application/json
Date: Sat, 07 Nov 2015 14:31:58 GMT
Server: WSGIServer/0.1 Python/2.7.10
Vary: Accept, Cookie
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

{
    "comments": [], 
    "email": "john@gmail.com", 
    "first_name": "John", 
    "id": 9, 
    "last_name": "Hitchcock", 
    "password": "pbkdf2_sha256$20000$gxcMMbFo4Syj$q66fyJK1JJmiD/OOKEE4jLmAStj8ZlJjvBSGNWQhcNk=", 
    "username": "John"
}
```


**3. One user cannot see the details of other users**
User cannot access the details of other users not he can list all the users
```
PRINHYLTPAP0472:~ swapnild$ http -a James:James123 https://movie-database-api.herokuapp.com/users/7/
HTTP/1.1 403 FORBIDDEN
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Connection: close
Content-Type: application/json
Date: Sat, 07 Nov 2015 14:37:38 GMT
Server: WSGIServer/0.1 Python/2.7.10
Vary: Accept, Cookie
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

{
    "detail": "You do not have permission to perform this action."
}
```

But he can access his own details and can also update the details
```
PRINHYLTPAP0472:~ swapnild$ http -a James:James123 https://movie-database-api.herokuapp.com/users/6/
HTTP/1.1 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Connection: close
Content-Type: application/json
Date: Sat, 07 Nov 2015 14:37:43 GMT
Server: WSGIServer/0.1 Python/2.7.10
Vary: Accept, Cookie
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

{
    "comments": [
        "https://movie-database-api.herokuapp.com/commets/9/"
    ], 
    "email": "James123@gmail.com", 
    "first_name": "James", 
    "id": 6, 
    "last_name": "Whale", 
    "password": "pbkdf2_sha256$20000$eMiVisBdAGsL$XzKGeV0/zt2pWzyK91bsB9PyWGtUBse4Y31zTdwZYhU=", 
    "username": "James"
}
```

These are similar other permissions applied like admin user cannot add comments on movies but admin can delete the comments.


#### Commets
Registed users can add comments on the movies
```
$ http -a James:James123 POST https://movie-database-api.herokuapp.com/commets/ movie=3 comment="Fantastic Movie.. Must watch"
HTTP/1.1 201 CREATED
Allow: GET, POST, HEAD, OPTIONS
Connection: close
Content-Type: application/json
Date: Sat, 07 Nov 2015 15:08:03 GMT
Location: https://movie-database-api.herokuapp.com/commets/11/
Server: WSGIServer/0.1 Python/2.7.10
Vary: Accept, Cookie
Via: 1.1 vegur
X-Frame-Options: SAMEORIGIN

{
    "comment": "Fantastic Movie.. Must watch", 
    "movie": 3, 
    "owner": "James", 
    "url": "https://movie-database-api.herokuapp.com/commets/11/"
}
```
