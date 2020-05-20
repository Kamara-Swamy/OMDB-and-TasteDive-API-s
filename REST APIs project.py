#This code might not be reusable because you can find any "request_with_caching" module in python but can you can develop your own,
#the purpose is understand how api works and in this code is written to extract movies names, if you want to write query on other things 
# you can visit the api file provided and give the required parameters in param attribute in requests_with_caching.get function.


import requests_with_caching
import json

def get_movies_from_tastedive(string):
    baseurl = "https://tastedive.com/api/similar"
    name = {}
    name["q"] = string
    name["type"] = "movies"
    name["limit"] = 5
    final = requests_with_caching.get(baseurl, params = name)
    print(final.url)
    x = json.loads(final.text, indent = 4)
    return(x)
	

print("----------------------------")  


def extract_movie_titles(file):
    result = []
    for x in file['Similar']['Results']:
        result.append(x['Name'])
    return result

print("----------------------------")  
def get_related_titles(movies):
    if movies!= []:
        result =[]
        for movie in movies:
            res = extract_movie_titles(get_movies_from_tastedive(movie))
            [result.append(x) for x in res if x not in result]
        return result
    else:
        return movies

print("----------------------------")  



def get_movie_data(string):
    baseurl = "http://www.omdbapi.com/"
    name = {}
    name['t'] = string
    name['r'] = 'json'
    final = requests_with_caching.get(baseurl , params = name)
    print(final.url)
    x = final.json()
    return x

print("----------------------------") 

def get_movie_rating(file):
    val= ''
    for x in file['Ratings']:
        if x['Source'] == 'Rotten Tomatoes':
            val = x['Value']
    if val != '':
        rating = int(val[:2])
    else:
        rating = 0
    return rating
    
print("----------------------------") 

def get_sorted_recommendations(titles):
    elements = get_related_titles(titles)
    title = sorted(elements, key = lambda element: (get_movie_rating(get_movie_data(element)), element), reverse = True)
    return title
# You can call the function as below by passing arguments you like.
#print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])) 
    
