from flask_frozen import Freezer
from app import app
freezer = Freezer(app)
app.config['FREEZER_IGNORE_404_NOT_FOUND'] = False
from datafoo import get_wrangled_data

wrangled_data = get_wrangled_data()

@freezer.register_generator
def detail():
    businesses = set([datum['business_id'] for datum in wrangled_data])
    for business in businesses:
        if '/' in business:
            continue
        yield '/business/' + business + '.html'

@freezer.register_generator
def price_detail():
    prices = set([datum['yelp_price'] for datum in wrangled_data])
    for price in prices:
        if '/' in price:
            continue
        yield '/price/' + price + '.html'

@freezer.register_generator
def category_detail():
    categories = set([datum['yelp_category'] for datum in wrangled_data])
    for category in categories:
        if '/' in category:
            continue
        yield '/category/' + category + '.html'


@freezer.register_generator
def rating_detail():
    ratings = set([datum['yelp_rating'] for datum in wrangled_data])
    for rating in ratings:
        if '/' in rating:
            continue
        yield '/rating/' + rating + '.html'


if __name__ == '__main__':
    freezer.freeze()