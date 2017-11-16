# Component Design
## Component List
### Clean data:
This component will be used for all of the use cases defined by us in our functional design specification. We will perform the data cleaning exercise based on the features we see fit for our analysis. Examples of a few relevant features include, number of beds, number of bathrooms, price of the Airbnb listing etc.

### Count restaurants by zip code:
This component is relevant to all use cases in our functional specification document. Once we clean the both the Airbnb and the restaurants data, the next step would be to count the number of restaurants in every zip code and store it in a separate variable for later use.

### Plotting the Airbnb and restaurant locations on a map of New York City:
This component will be used to address the 1st and 2nd use cases in our functional design specification. This component will be helpful in visualizing the distribution of various Airbnb listings and restaurants in New York City & will help the user in navigating the different features which might be of interest to him/her.

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

### plotmap()
* **What it does:** Maps all restaurants and Airbnb listings according to their location coordinates
* **Inputs:**
	* airbnb_df.latitude
	* airbnb_df.longitude
	* restaurant_df.latitude
	* restaurant_df.longitude
* **Outputs:** A map with an interactive layer which can be hovered over to see the details of every Airbnb listing and restaurants in the NY area
* **How it works:** Uses plotly library and Google Maps’ API to plot Airbnb listings as well as restaurants.
```
Pseudo Code:
* Import bokeh library
* From bokeh.models import GMapPlot to plot Google Maps as our background
* Plot map and define the latitude and longitude range for NYC
* Plot the data points from the airbnb and restaurant dataframes as different colored circles
* Add other tools so the user can control and interact with the map
```

### Name: predict_price()
* **What it does:** Makes a prediction of the price of an Airbnb listing based on certain parameters.
* **Inputs:** 
	* Number of beds, baths of the Airbnb listing
	* Number of restaurants in the region
	* Trained model based on existing data
* Output: A floating point value describing the projected cost of the Airbnb listing based on the input parameters.
* How it works: Uses the model developed using supervised learning on existing data to make a prediction for the cost of the Airbnb listing based on the input values of beds and baths, number of restaurants in the region.
```
Pseudo Code:
	* Perform a sanity check on the input values (make sure they are positive, etc)
	* Pass the input values to the trained model
	* Return the value obtained from the trained model and render the value on the UI
```
