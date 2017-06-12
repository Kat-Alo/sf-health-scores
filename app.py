import csv
from flask import Flask
from flask import render_template
from operator import itemgetter
from datetime import date, datetime, time
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
    for i in all_inspections:
        i['inspection_date'] = datetime.strptime(str(i['inspection_date'])[:10], "%m/%d/%Y")
    new_list = sorted(all_inspections, key=itemgetter('inspection_date'), reverse=True)
    most_recent = []
    for n in new_list:
        if n.get('business_address') not in [d['business_address'] for d in most_recent]:
            if n.get('inspection_score') is not '':
                most_recent.append(n)

    most_recent = sorted(most_recent, key=itemgetter('business_name'))

    return most_recent



@app.route("/")
def index():
    template = 'index.html'
    object_list = get_abbrev_csv()
    return render_template(template, object_list=object_list)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
