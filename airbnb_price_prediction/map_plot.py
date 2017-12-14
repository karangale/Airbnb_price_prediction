"""Clean data and plot a map of airbnb listings and restaurants."""

import pandas as pd
import folium
from cleaning_utils import clean_restraunts_geo
from cleaning_utils import clean_airbnb
from folium.plugins import MarkerCluster
from markers import airbnb_popup_frame

# Import Restaurant Geocoded data and clean it for required rows
rest_geo_df = pd.read_csv('./Data/NYC_Restaurants_Geocoded_-_Sheet1.csv')
rest_geo = clean_restraunts_geo(rest_geo_df)

# Import airbnb data and clean the airbnb data for the required rows
airbnb_data = pd.read_csv('./Data/listings.csv')
airbnb_data = clean_airbnb(airbnb_data)

# Centralize the map on New York City
NY_COORDINATES = (40.730610, -73.935242)

map = folium.Map(location=NY_COORDINATES, zoom_start=10)
marker_cluster = MarkerCluster()

for each in rest_geo.iterrows():
    popup = folium.Popup(each[1]['Name'].title(), parse_html=True)
    folium.Marker(
        [each[1]['Latitude'], each[1]['Longitude']],
        popup=popup,
        icon=folium.Icon(icon='cutlery',
                         color='red')).add_to(marker_cluster)
r = folium.FeatureGroup(name='Restaurants')
r.add_child(marker_cluster)
map.add_child(r)

# Create map cluster for airbnb listings
marker_cluster_airbnb = MarkerCluster()
# Create each marker and plot it on the map
for each in airbnb_data[1:20000].iterrows():
    popup = airbnb_popup_frame(each[1])
    folium.Marker([each[1]['latitude'], each[1]['longitude']], popup=popup,
                  icon=folium.Icon(icon='home',
                  color='blue')).add_to(marker_cluster_airbnb)
a = folium.FeatureGroup(name='Airbnb')
a.add_child(marker_cluster_airbnb)
map.add_child(a)

# Add layers for restaurants and airbnb listings
map.add_child(folium.LayerControl())

# Save the map to an html file
map.save('/templates/airbnb_restaurant.html')
