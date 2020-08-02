import requests



def getMovie(genre):
    api = "https://run.mocky.io/v3/2e0ef401-7da0-42e7-acee-6fb958e9b9e0" 
    moviesData = requests.get(api).json()
    genre = genre.capitalize()
    print(genre) 
    stringOfMovies=""
    for movie in moviesData:
        if (genre in movie['genres']):
            stringOfMovies = stringOfMovies  + "------" + movie['title']  

    return stringOfMovies



