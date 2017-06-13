import requests
from os import makedirs
from os.path import exists, join, basename
import json
from datafoo import get_abbrev_data, WRANGLED_DATA_PATH, WRANGLED_HEADERS
from time import sleep
import csv

SEARCH_BASE_URL = 'https://api.yelp.com/v3/businesses/search' #?term={business_name}&latitude={business_latitude}&&longitude={business_longitude}'
RESULT_BASE_URL = 'https://api.yelp.com/v3/businesses/{id}'
access_token = "MvLQh-YJW_UNFXJcI5qHLKznwUWlkTnl1N1tFofn34eWVa0X4gWcuNpA-qSaiVOMwsbdmcG-kOQUytP8ADd-yXjxWWAvlXS8-Pnof76_DAc59DOMXQHIHVh7kl4_WXYx"



def search_yelp(name, latitude, longitude):
    headers = {'Authorization': 'bearer %s' % access_token}
    params = {'location': 'San Francisco', 'term': name, 'latitude': latitude, 'longitude': longitude}
    resp = requests.get(url=SEARCH_BASE_URL, params=params, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    else:
        return False

def get_yelp_business_data(name, latitude, longitude):
    results = search_yelp(name, latitude, longitude)
    if results:
        businesses = results.get('businesses')
        if businesses:
            return businesses[0]
    return {}


def batch_download_yelp_data(delaytime=1):
    records = get_abbrev_data()
    for row in records:
        saved_fname = join('static', 'yelpdata', row['business_id'] + '.json')
        if exists(saved_fname):
            print("Already have {fname} ({bizname})...".format(fname=saved_fname, bizname=row['business_name']))
        elif row['business_latitude'] == '':
            print('{id} {bizname} has no latitude/longitude'.format(id=row['business_id'], bizname=row['business_name']))
        else:
            print("Writing {fname} ({bizname})".format(fname=saved_fname, bizname=row['business_name']))
            biz = get_yelp_business_data(row['business_name'],
                    latitude=row['business_latitude'], longitude=row['business_longitude'])
            sleep(delaytime)
            with open(saved_fname, 'w') as f:
                txt = json.dumps(biz, indent=2)
                f.write(txt)



def wrangle_yelp_data():
    outfile = open(WRANGLED_DATA_PATH, 'w')
    outcsv = csv.DictWriter(outfile, fieldnames=WRANGLED_HEADERS)
    outcsv.writeheader()
    for row in get_abbrev_data():
        saved_fname = join('static', 'yelpdata', row['business_id'] + '.json')
        if exists(saved_fname):
            f = open(saved_fname, 'r')
            yelpdatum = json.load(f)

            if yelpdatum and yelpdatum.get('price'):
                row['yelp_rating'] = yelpdatum['rating']
                row['yelp_price'] = yelpdatum['price']
                row['yelp_review_count'] = yelpdatum['review_count']
                # write wrangled thing
                outcsv.writerow(row)
    outfile.close()



# def get_yelp_data(business_name, latitude, longitude):
#     dir_name = business_name + "_business"
#     data_fname = dir_name + "id.json"
#     name = business_name
#     # name.replace(" ", "+")
#     url = 'https://api.yelp.com/v3/businesses/search'
#     # url = SEARCH_BASE_URL.format(business_name=name , business_latitude=business['business_latitude'], business_longitude=business['business_longitude'])

#     fetch_yelp_data(url, data_fname, dir_name, name, latitude, longitude)
#     f = open(data_fname, 'r')
#     raw_data = f.read()
#     f.close()
#     json_file = json.loads(raw_data)
#     return json_file


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

# def add_yelp_data(business_list):
#     for b in business_list:
#         json_file = get_yelp_data(b)
#         b['price'] = json_file["businesses"][0]["price"]
#         b['yelp_rating'] = json_file["businesses"][0]["rating"]
#         b['yelp_url'] = json_file["businesses"][0]['url']
#         b['category'] = json_file["businesses"][0]["categories"][0]["title"]

#     return business_list




# def fetch_yelp_data(url, data_fname, dir_name, name, latitude, longitude):
#     if exists(data_fname):
#         pass
#     else:
#         makedirs(dir_name, exist_ok = True)
#         headers = {'Authorization': 'bearer %s' % access_token}
#         params = {'location': 'San Francisco', 'term': name, 'latitude': latitude, 'longitude': longitude}
#         resp = requests.post(url=url, params=params, headers=headers)
#         with open(data_fname, 'wb') as f:
#             f.write(resp.content)


