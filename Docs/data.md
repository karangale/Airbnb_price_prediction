# Requirements:

Our analysis focusses on understanding the presence of restaurants on Airbnb listings in New York City. We are looking at the variation in the prices of the Airbnb listings based on the presence of restaurants. The datasets used for this analysis are publicly available. The list of requirements in order to perform a thorough analysis are as follows:

> - Both the datasets are at a location level which would be the feature used for merging the datasets. Specifically, the merge condition would be on the zip codes of the listings and the restaurants.
> - The other metric we are looking at is the average distance between the listings and the restaurants in the area. For this we would use the co-ordinates of the listings and the restaurants and decode the co-ordinates in Python.
> - For looking at the type of restaurants that are more popular in an area, we could cluster the restaurants based on their type.
> - For analyzing the variation in the prices of the listings, we also need price as a column in the Airbnb listings dataset.

# Sources:
We have two databases that we plan to use for this project.

| Dataset                      | Content                                                                                              | Availability                                                                                           | Source                                                                                                 |
|------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| listings.csv.gz              | Detailed Airbnb listings for New York City. It is 149 MB in size and has 41,188 rows and 95 columns  | This data is publicly available information from the Airbnb website under a  Creative Commons Liscence | http://insideairbnb.com/get-the-data.html                 |
| NYC Restaurants Geocoded.csv | This contains a list of restaurants in  New York City with their geo-coded locations                 | This data has been made available by  Miles Grimshaw on his website                                    | http://milesgrimshaw.com/nyc-restaurant-database/ |

# Evaluation:
|                                                                                             | AirBnb Listings | NYC Restaurant Data |
|---------------------------------------------------------------------------------------------|:---------------:|:--------------------:|
| Is there a correlation between the no. of restaurants in NYC and the no. of Airbnb listings |       Used      |                Used |
| How does the price of Airbnb listings vary according to the presence of restaurants         |       Used      |                Used |
