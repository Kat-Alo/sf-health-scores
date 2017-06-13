from flask import Flask
from flask import render_template

from flask import abort
from datafoo import get_wrangled_data, get_full_data
# from yelp import add_yelp_data
app = Flask(__name__)


@app.route("/")
def index():
    template = 'index.html'
    object_list = get_wrangled_data()
    return render_template(template, object_list=object_list)

@app.route('/business/<biz_id>')
def detail(biz_id):
    template = 'detail.html'

    inspection_list = []
    business = None

    for row in get_wrangled_data():
        if row['business_id'] == biz_id:
            business = row
            break


    if not business:
        abort(404)
    else:
        for row in get_full_data():
            if row['business_id'] == biz_id:
                    inspection_list.append(row)
        return render_template(template, inspections=inspection_list, business=business)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)














