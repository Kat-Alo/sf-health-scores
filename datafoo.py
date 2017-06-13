import csv
from operator import itemgetter
from datetime import date, datetime, time
from os.path import join


ABBREV_PATH = './static/sf-most-recent.csv'
FULL_PATH = './static/sf-health-data.csv'
WRANGLED_DATA_PATH = join('static', 'sf-yelp-wrangled.csv')

WRANGLED_HEADERS =  ["business_name",
"yelp_rating", "yelp_price", "yelp_review_count",
"inspection_score","business_latitude","inspection_type","business_city","risk_category",
"business_location","business_phone_number","inspection_id","business_id","business_address","inspection_date",
"violation_description","violation_id","business_longitude","business_state","business_postal_code"]




def get_full_data():
    csv_path = FULL_PATH
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list


def get_abbrev_data():
    csv_path = ABBREV_PATH
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = sorted(csv_obj, key=itemgetter('business_name'))

    return csv_list


def get_wrangled_data():
    csv_path = WRANGLED_DATA_PATH
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = sorted(csv_obj, key=itemgetter('business_name'))

    return csv_list

# data wrangling stuff...

#creating a main view table based only on most recent inspection results
# def get_abbrev_csv():
#     all_inspections = get_full_data()

#     #change date strings to datetime objects to find most recent inspections for each restaurant
#     for i in all_inspections:
#         i['inspection_date'] = datetime.strptime(str(i['inspection_date'])[:10], "%m/%d/%Y")
#     #sort list from most recent inspection to earliest inspection
#     new_list = sorted(all_inspections, key=itemgetter('inspection_date'), reverse=True)
#     most_recent = []

#     #add most recent inspection for each restaurant that has a health score
#     for n in new_list:
#         if n.get('business_address') not in [d['business_address'] for d in most_recent]:
#             if n.get('inspection_score') is not '':
#                 most_recent.append(n)
#     return most_recent


# def combine_with_yelp
#     #sort list by restaurant name to make more navigable
#     most_recent = sorted(most_recent, key=itemgetter('business_name'))
#     most_recent = add_yelp_data(most_recent)
#     return most_recent

