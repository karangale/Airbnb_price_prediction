# Predicting Airbnb listing prices based on the presence of restaurants nearby:
We are analyzing the effect of restaurants and eateries on Airbnb listings in New York City. We have chosen New York City as it is one of the largest and most popular tourist destinations in the world with a large amount of Airbnb listings.

## Questions:
We are looking to answer the following questions using the data:
* Is there a correlation between the number of restaurants in a particular area and the number of Airbnb listings in that area?
* How does the price of Airbnb listings vary according to the presence of restaurants in that region?

## Data Sources:
The data we are using comes from the [Airbnb website](http://data.insideairbnb.com/united-states/ny/new-york-city/2016-07-02/visualisations/listings.csv) and the restaurant data is pulled from the [NYC restaurant database](https://mgrimshaw.carto.com/tables/nytimes_nyc_restaurants/public) published by Miles Grimshaw.

![alt text](http://www.hotelnewsnow.com/Media/Default/Legacy//FeatureImages/airbnb_newyork.jpg "Image 1")

## Installation:
1. Clone the git repository to a local location on your machine by downloading the zip file or typing the following in a terminal:
```
git clone https://github.com/UWSEDS-aut17/uwseds-group-team-star.git
```

2. Open the main 'uwseds-group-team-star folder' and run the setup by typing the following:
```
python setup.py install
```

3. Download the Airbnb 'listings.csv.gz' file:
[listings.csv.gz](http://data.insideairbnb.com/united-states/ny/new-york-city/2017-10-02/data/listings.csv.gz)

4. Extract the 'listings.csv' file and save it to the data folder in the following location:
```
uwseds-group-team-star/airbnb_price_prediction/Data
```

5. Open Command Prompt or Terminal as Administrator and navigate to the airbnb_price_prediction folder in the repository.
```
uwseds-group-team-star/airbnb_price_prediction
```

6. Execute the following commands one by one in the airbnb_price_prediction folder
```
python create_frontpage.py
```

If you have Windows (Command Prompt):
```
set FLASK_APP=create_frontpage.py
python -m flask run
```

If you have Linux/Mac (Terminal):
```
export FLASK_APP=create_frontpage.py
python -m flask run
```

7. Run the visualization by typing the following url into your preferred web browser:
```
http://127.0.0.1:5000
```

8. Click on the links on the web page to open that particular module.

## Using the Price Prediction Module:
* This module allows you to get the predicted price of an Airbnb listing depending on the input parameters.
* Type in the specified parameters.
* Click on 'Submit' button to view the predicted listing price.

<p align="center">
  <img src="https://github.com/UWSEDS-aut17/uwseds-group-team-star/raw/master/Examples/ML_Example.PNG">
 </p>
 <p align="center">

## Using the 'Mapping the Listings':
* This module allows you to view the Airbnb listings on an interactive map.
* You can choose to zoom in on various clusters of airbnb and restaurant listings by clicking on them.
* Airbnb listings have blue markers with a house icon, while restaurants have red markers with a fork and knife icon.
* If you want to only view airbnb listings or restaurants, you can click on the layers on the top right corner of the map to filter them.
* Click on a particular listing to view more details and find a link to book that particular listing.

<p align="center">
  <img src="https://github.com/UWSEDS-aut17/uwseds-group-team-star/raw/master/Examples/New%20York%20Map.PNG">
 </p>
 <p align="center">
  <img src="https://github.com/UWSEDS-aut17/uwseds-group-team-star/raw/master/Examples/airbnb_listing.PNG">
</p>
