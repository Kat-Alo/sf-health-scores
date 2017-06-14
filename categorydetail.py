from datafoo import get_wrangled_data



def get_price_data(price):
    price_data = []

    wrangled_data = get_wrangled_data()

    for row in wrangled_data:
        if row['yelp_price'] == price:
            price_data.append(row)

    return price_data

def get_category_data(category):
    category_data = []

    wrangled_data = get_wrangled_data()

    for row in wrangled_data:
        if row['yelp_category'] == category:
            category_data.append(row)

    return category_data

def get_rating_data(rating):
    rating_data = []

    wrangled_data = get_wrangled_data()

    for row in wrangled_data:
        if row['yelp_rating'] == rating:
            rating_data.append(row)

    return rating_data
