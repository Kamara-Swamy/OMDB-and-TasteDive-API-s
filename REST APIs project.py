'''This project will take you through the process of mashing up data from two different APIs to make movie recommendations.
You will put those two together. You will use TasteDive to get related movies for a whole list of titles.
You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores'''

import requests
import json


def get_movies_from_tastedive(string):
    baseurl = "https://tastedive.com/api/similar"
    name = {}
    name["q"] = string
    name["type"] = "movies"
    name["limit"] = 5
    final = requests.get(baseurl, params=name)
    print(final.url)
    x = json.loads(final.text)
    return (x)


def extract_movie_titles(file):
    result = []
    for x in file['Similar']['Results']:
        result.append(x['Name'])
    return result


def get_related_titles(movies):
    if movies != []:
        result = []
        for movie in movies:
            res = extract_movie_titles(get_movies_from_tastedive(movie))
            [result.append(x) for x in res if x not in result]
        return result
    else:
        return movies

def get_movie_data(string):
    baseurl = "http://www.omdbapi.com/"
    name = {}
    name['apikey'] = "8edc265e"
    name['t'] = string
    name['r'] = 'json'
    final = requests.get(baseurl, params=name)
    print(final.url)
    x = final.json()
    return x



def get_movie_rating(file):
    val = ''
    for x in file['Ratings']:
        if x['Source'] == 'Rotten Tomatoes':
            val = x['Value']
    if val != '':
        rating = val[:3]
    else:
        rating = 0
    return rating



def get_sorted_recommendations(titles):
    elements = get_related_titles(titles)
    title = sorted(elements, key=lambda element: (get_movie_rating(get_movie_data(element)), element), reverse=True)
    return title
# You can call the function as below by passing arguments you like.
print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))
