import csv
from flask import Flask
from flask import render_template
from operator import itemgetter
from datetime import date, datetime, time
from flask import abort
from yelp import add_yelp_data
app = Flask(__name__)

def get_full_csv():
    csv_path = './static/sf-health-data.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

#creating a main view table based only on most recent inspection results
def get_abbrev_csv():
    all_inspections = get_full_csv()

    #change date strings to datetime objects to find most recent inspections for each restaurant
    for i in all_inspections:
        i['inspection_date'] = datetime.strptime(str(i['inspection_date'])[:10], "%m/%d/%Y")
    #sort list from most recent inspection to earliest inspection
    new_list = sorted(all_inspections, key=itemgetter('inspection_date'), reverse=True)
    most_recent = []

    #add most recent inspection for each restaurant that has a health score
    for n in new_list:
        if n.get('business_address') not in [d['business_address'] for d in most_recent]:
            if n.get('inspection_score') is not '':
                most_recent.append(n)

    #sort list by restaurant name to make more navigable
    most_recent = sorted(most_recent, key=itemgetter('business_name'))
    most_recent = add_yelp_data(most_recent)
    return most_recent


@app.route("/")
def index():
    template = 'index.html'
    object_list = get_abbrev_csv()
    return render_template(template, object_list=object_list)

@app.route('/<name>/')
def detail(name):
    template = 'detail.html'
    object_list = get_abbrev_csv()
    full_list = get_full_csv()
    business_list = []
    for row in object_list:
        if row['business_name'] == name:
            for f in full_list:
                if f['business_name'] == name:
                    business_list.append(f)
            return render_template(template, object_list=business_list)
    abort(404)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)














