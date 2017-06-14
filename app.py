from flask import Flask
from flask import render_template
from categorydetail import get_price_data, get_category_data, get_rating_data
from flask import abort
from datafoo import get_wrangled_data, get_full_data

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

@app.route('/price/<biz_price>')
def price_detail(biz_price):
    template = 'pricedetail.html'

    business_list = get_price_data(biz_price)

    return render_template(template, business_list=business_list, biz_price=biz_price)

@app.route('/category/<biz_category>')
def category_detail(biz_category):
    template = 'categorydetail.html'

    business_list = get_category_data(biz_category)

    return render_template(template, business_list=business_list, biz_category=biz_category)

@app.route('/rating/<biz_rating>')
def rating_detail(biz_rating):
    template = 'ratingdetail.html'

    business_list = get_rating_data(biz_rating)

    return render_template(template, business_list=business_list, biz_rating=biz_rating)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)














