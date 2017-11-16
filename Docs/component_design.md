# Component Design
## Component List
### Clean data:
This component will be used for all of the use cases defined by us in our functional design specification. We will perform the data cleaning exercise based on the features we see fit for our analysis. Examples of a few relevant features include, number of beds, number of bathrooms, price of the Airbnb listing etc.

### Count restaurants by zip code:
This component is relevant to all use cases in our functional specification document. Once we clean the both the Airbnb and the restaurants data, the next step would be to count the number of restaurants in every zip code and store it in a separate variable for later use.

## Component Specification
### clean_data()
* **What it does:** This component would be used to clean the restaurants as well as the Airbnb listing data by retaining only the relevant features for use in our analysis.
* **Inputs:**
	* **restaurants.csv:** Restaurants listing file
	* **listings.csv:** Airbnb listings file
	* **NYC Restaurants Geocoded.csv:** Restaurants with their respective latitude and
longitude
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

### count_restaurants()
* **What it does:** Counts number of restaurants in each zip code in New York City
* **Inputs:** The restaurant dataframe created as part of clean_data() step 
* **Outputs:** A dataframe which gives the count of restaurant in each zip code
* **How it works:**
```
Pseudo Code:

	* Use the groupby operation within pandas to groupby on the zip code variable within the dataframe
	* restaurants_count_df = cleaned_restaurants_df.groupby(‘zipcode’).count()
	* return restaurants_count_df
```
