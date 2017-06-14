import requests
from os import makedirs
from os.path import exists, join, basename
import json
from datafoo import get_abbrev_data, WRANGLED_DATA_PATH, WRANGLED_HEADERS
from time import sleep
import csv

SEARCH_BASE_URL = 'https://api.yelp.com/v3/businesses/search' #?term={business_name}&latitude={business_latitude}&&longitude={business_longitude}'
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
                row['yelp_category'] = yelpdatum['categories'][0]['title']

                # write wrangled thing
                outcsv.writerow(row)
    outfile.close()




