This app allows users to explore SF restaurant health scores against other traits (e.g. average meal price and types of dish).

# SF Restaurant Health Inspection Mapper

## Elevator Pitch

Data is openly available from the city of San Francisco on restaurant health inspection records. Updates to these records have inspired pieces on the least sanitary restaurants in the city and has allowed Yelp to incorporate a health score in each restaurant profile. This tool will allow users to view the health inspection records of restaurants in San Francisco by popularity and price.

The aim of this tool will be to easily answer the questions: (1) of the most expensive restaurants in San Francisco, which have poor health inspection scores? (2) Of the most popular restaurants in San Francisco, which have poor health inspection scores? This tool should also help identifty interesting changes in scores. For instance, if a restaurant that 'should' receive good health scores, based on either popularity or cost, receives a lower inspection score, the map should draw attention to that new data.

## Inspirations and Prior Work

- [HDScores](https://itunes.apple.com/us/app/hdscores/id892798039?mt=8): An app made for iPhone that allows users to view restaurant health inspection codes on map. The application does only that, however, and does not allow users to filter restaurant results on the map.
- [What the Health App](https://www.whatthehealthapp.com/): This is another mobile app that allows users to view restaurant health inspection codes on a map. The application appears better designed and seems to include more restaurant review and profile features along with the health scores.
- [Fatal Force](https://www.washingtonpost.com/graphics/national/police-shootings-2017/): This application obviously does not perform a similar function, but I have included it to illustrate how I would like to improve on previous applications. The Washington Post took a figure of interest (namely, the number of people killed by police officers) and allowed users to better understand that figure by filtering it through factors of interest (e.g. whether the person was armed or mentally ill, the location, and their gender).

## Articles

- [These San Francisco restaurants received a 'poor' grade on their restaurant safety scores](http://www.sfgate.com/food/article/These-San-Francisco-restaurant-s-received-a-7745836.php): The piece's main focus is a gallery of images, each one representing a San Francisco restaurant that received a 'poor' health score. There is a brief written article explaining the source of the health scores, and there is a video showing the most common health code infractions that could lead to a 'poor' score.
- [These San Francisco restaurants failed health inspections recently](http://www.sfgate.com/food/article/San-Francisco-restaurants-failed-health-10874533.php): Similarly to the piece above, this article shows an image gallery of the restaurants that failed their health inspections, along with a brief written piece on the meaning of a failed inspection and the same video of the most common health code infractions.
- [SF Restaurants With Poor Health Ratings Can Now Buy Opportunity for New Scores](http://www.nbcbayarea.com/news/local/SF-Restaurants-With-Poor-Health-Ratings-Can-Now-Buy-Opportunity-for-New-Scores-411721205.html): This article discusses the new pilot health inspection system that allows restaurants to buy a do-over inspection. Inspections are conducted randomly and without notice. While restaurants must correct any infractions immediately, they may have to bear that lower score until whenever their next surprise inspection occurs. Critics say this allows restaurants to cover up dirty practices. This could impact the legitimacy of the scores represented in this new application. However, if data is made available on whether a score was the result of one of these 'do-over' inspections, that could also be included in the map view.

## Data Sources

San Francisco is one of several cities that report their [restaurant health scores](https://data.sfgov.org/Health-and-Social-Services/Restaurant-Scores-LIVES-Standard/pyih-qa8i/data) to Yelp in a standardized and more easily read format called [Local Inspector Value-Entry Specification](https://www.yelp.com/healthscores/feeds) (LIVES).

I will also use Google Maps to create the map itself and locate the restaurants based either on coordinates or street address.
