# Functional Specifications


## Problem Statement
Analyze the effect of restaurants and eateries on Airbnb listings in New York City and build a predictive model to predict the price of an Airbnb listing based on this.


## User Profile
The user is assumed have a basic understanding of using the internet and maps. Our analysis is specific to New York city and a familiarity with the geography of New York City would make it easier for the user to navigate to different places of interest.


Furthermore, the user will need to have a familiarity with using Airbnb in order to understand the different customizations our application would provide, such as number of rooms, restaurant cuisines, etc, to visualize them on an interactive map.


## Elements of the problem statement


We can divide our problem statement in the following parts:


1. What is the effect of the number of restaurants in a region on the price of an Airbnb listing in that region?
2. Does the variety of cuisine offered in a region have an effect on the prices of the listing?
3. How does number of rooms in an Airbnb listing affect the price of the listing?


## Use Cases
**1. Search Airbnb listing**
   * User navigates through our interactive map which maps all Airbnb listings and restaurants in New York using simple clicks
   * User clicks on preferred Airbnb listing
   * Interface highlights all restaurants in the region
   * A dialog box displays information about the Airbnb listing along with it’s price


**2. Information about restaurants**
   * User clicks on restaurant on the interactive map
   * A dialog box displays information about the restaurant including type of cuisine and health grade


**3. Predict the Airbnb price depending on number of restaurants and number of rooms**
   * User enters the zipcode of the location he wants to stay in and the number of rooms they would prefer and clicks on the ‘Predict’ button
   * The API takes this information and feeds it to our pickled prediction model
   * The model returns the predicted price as the output with a 95% confidence interval