# Predicting Airbnb listing prices based on the presence of restaurants Nearby:
We are analyzing the effect of restraunts and eateries on Airbnb listings in New York City. We have chosen New York City as it is one of the largest and most popular tourist destinations in the world with a large amount of Airbnb listings.

## Questions:
We are looking to answer the following questions using the data:
* Is there a correlation between the number of restraunts in a particular area and the number of Airbnb listings in that area?
* How does the price of Airbnb listings vary according to the presence of restraunts in that region?

## Data Sources:
The data we are using comes from the [Airbnb website](http://insideairbnb.com/get-the-data.html) and the restraunt data is pulled from the [NYC restraunt database](https://mgrimshaw.carto.com/tables/nytimes_nyc_restaurants/public) published by Miles Grimshaw.

![alt text](http://www.hotelnewsnow.com/Media/Default/Legacy//FeatureImages/airbnb_newyork.jpg "Image 1")

## Installation:
1. Clone the git repository to a local location on your machine by downloading the zip file or typing the following in a terminal:
```
git clone https://github.com/UWSEDS-aut17/uwseds-group-team-star.git
```

2. Run the setup by typing the following:
```
python setup.py develop
```

3. Download the data files from the sources above and put them into the 'Data' folder in downloaded repository.

4. Run the visualization by typing the following url into your preferred web browser:
```
http://127.0.0.1:5000
```

5. Click on the links on the web page to open that particular module.

## Using the Price Prediction Module:
* Type in the specified parameters.
* Click on 'Predict Prices' button to view the predicted listing price.

## Using the Visual Map:
* You can choose to zoom in on various clusters of airbnb and restaurant listings by clicking on them.
* Airbnb listings have blue markers with a house icon, while restaurants have red markers with a fork and knife icon.
* If you want to only view airbnb listings or restaurants, you can click on the layers on the top right corner of the map to filter them.
* Click on a particular listing to view more details and find a link to book that particular listing.

<p align="center">
  <img src="https://github.com/UWSEDS-aut17/uwseds-group-team-star/blob/master/Examples/New%20York%20Map.PNG">
 </p>
 <p align="center">
  <img src="https://github.com/UWSEDS-aut17/uwseds-group-team-star/blob/master/Examples/airbnb_listing.PNG">
</p>
