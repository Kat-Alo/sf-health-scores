import requests
from os import makedirs
from os.path import exists, join, basename
import json

SEARCH_BASE_URL = 'https://api.yelp.com/v3/businesses/search?term={business_name}&latitude={business_latitude}&&longitude={business_longitude}'
RESULT_BASE_URL = 'https://api.yelp.com/v3/businesses/{id}'
access_token = "MvLQh-YJW_UNFXJcI5qHLKznwUWlkTnl1N1tFofn34eWVa0X4gWcuNpA-qSaiVOMwsbdmcG-kOQUytP8ADd-yXjxWWAvlXS8-Pnof76_DAc59DOMXQHIHVh7kl4_WXYx"

def fetch_data(url, data_fname, dir_name, name, latitude, longitude):
    if exists(data_fname):
        pass
    else:
        makedirs(dir_name, exist_ok = True)
        headers = {'Authorization': 'bearer %s' % access_token}
        params = {'location': 'San Francisco', 'term': name, 'latitude': latitude, 'longitude': longitude}
        resp = requests.get(url=url, params=params, headers=headers)
        with open(data_fname, 'wb') as f:
            f.write(resp.content)

def get_yelp_data(business):
    dir_name = business['business_name'] + "_business"
    data_fname = dir_name + "id.json"
    name = business['business_name']
    # name.replace(" ", "+")
    url = 'https://api.yelp.com/v3/businesses/search'
    # url = SEARCH_BASE_URL.format(business_name=name , business_latitude=business['business_latitude'], business_longitude=business['business_longitude'])
    latitude = business['business_latitude']
    longitude = business['business_longitude']
    fetch_data(url, data_fname, dir_name, name, latitude, longitude)
    f = open(data_fname, 'r')
    raw_data = f.read()
    f.close()
    json_file = json.loads(raw_data)
    return json_file


# def get_yelp_data(business):
#     id = get_id(business)
#     dir_name = business['business_name'] + "_profile"
#     data_fname = dir_name + "info.json"
#     url = RESULT_BASE_URL.format(id=id)

#     fetch_data(url, data_fname, dir_name)
#     f = open(data_fname, 'r')
#     raw_data = f.read()
#     f.close()
#     return json.loads(raw_data)

def add_yelp_data(business_list):
    for b in business_list:
        json_file = get_yelp_data(b)
        if "businesses" in json_file:
            if 'price' in json_file['businesses'][0]:
                b['price'] = json_file["businesses"][0]["price"]
                b['yelp_rating'] = json_file["businesses"][0]["rating"]
                b['yelp_url'] = json_file["businesses"][0]['url']
                b['category'] = json_file["businesses"][0]["categories"][0]["title"]
        else:
            b['price'] = "Yelp does not have price data on this business."
            b['yelp_rating'] = "Yelp does not have a rating for this business."
            b['yelp_url'] = "Yelp does not have a profile for this business."
            b['category'] = "Yelp does not have a category for this business."

    return business_list



