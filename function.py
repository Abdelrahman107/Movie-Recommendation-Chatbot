
import requests
global response



def getMovie(genre):
  
    api = "https://run.mocky.io/v3/a6f18c23-7cee-4a7f-b4ac-11b9467af046" 
    moviesData = requests.get(api).json()
    #print(type(moviesData[0]['genres']))
    #list=['abc']
    #print(list)   
    genre=genre[0].upper()
    for movie in moviesData:
        if genre in movie['genres']:
            print(movie['title'])  
            #list.insert(movie['title'])

    #response = requests.get(api).json()
    #return response

