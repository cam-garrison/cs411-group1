import requests
import json
from settings import google_key


def find_stores(search_query):

    api_key = google_key

    # url variable store url
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # The text string on which to search'

    # get method of requests module
    # return response object
    r = requests.get(url + 'query=' + search_query +
                     '&key=' + api_key)

    # json method of response object convert
    #  json format data into python format data
    x = r.json()

    # now x contains list of nested dictionaries
    # we know dictionary contain key value pair
    # store the value of result key in variable y
    y = x['results']
    print(len(y))
    return y


find_stores(search_query='fashion stores in boston')
