#Component Design
##Component List
###Clean data:
This component will be used for all of the use cases defined by us in our functional design specification. We will perform the data cleaning exercise based on the features we see fit for our analysis. Examples of a few relevant features include, number of beds, number of bathrooms, price of the Airbnb listing etc.

##Component Specification
### clean_data()
* **What it does:** This component would be used to clean the restaurants as well as the Airbnb listing data by retaining only the relevant features for use in our analysis.
* **Inputs:** 
* **listings.csv:** Airbnb listings file
	* **restaurants.csv:** Restaurants listing file
	* **NYC Restaurants Geocoded.csv:** Restaurants with their respective latitude and longitude
* **Outputs:** 
	* airbnb_df
	* restaurant_df
* **How it works:** 
	* Read the two csv files into dataframes using pandas
```
Pseudo Code:
Import pandas as pd

airbnb_df = read listings data
restaurant_df = read restaurant data
```
