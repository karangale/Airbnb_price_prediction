def splitZip(zipcode):
    zips = zipcode.split("-")
    zipsDot = zips[0].split(".")
    zipsN = zipsDot[0].split("\n")
    return zipsN[0]
    
def clean_airbnb(airbnb_data_req):
    columns_interest_airbnb = ['street', 'neighbourhood','zipcode', 'latitude', 'longitude', 'property_type', 'accommodates', 
                               'bathrooms', 'bedrooms', 'beds', 'price', 'minimum_nights', 'maximum_nights', 
                               'number_of_reviews', 'neighbourhood_group_cleansed']
    airbnb_data_req = airbnb_data_req[columns_interest_airbnb]
    index_drop = airbnb_data_req[airbnb_data_req['zipcode'].isnull()].index.tolist()
    airbnb_data_req = airbnb_data_req.drop(index_drop)
    airbnb_data_req = airbnb_data_req.reset_index(drop = True)
    
    airbnb_data_req["bathrooms"].fillna(0, inplace = True)
    airbnb_data_req["bedrooms"].fillna(0, inplace = True)
    airbnb_data_req["beds"].fillna(0, inplace = True)
    airbnb_data_req["neighbourhood"].fillna("", inplace = True)
    
    airbnb_data_req["price"] = airbnb_data_req["price"].str.replace('$', '')
    airbnb_data_req["price"] = airbnb_data_req["price"].str.replace(',', '')
    airbnb_data_req["price"] = airbnb_data_req["price"].astype(float)
    
    airbnb_data_req["zipcode"] = airbnb_data_req["zipcode"].astype(str)
    
    airbnb_data_req["zipcode"] = airbnb_data_req["zipcode"].apply(splitZip)
    airbnb_data_req= airbnb_data_req[airbnb_data_req['zipcode']!='1m']
    
    airbnb_data_req = airbnb_data_req[airbnb_data_req['property_type'] == 'Apartment']
    
    return airbnb_data_req

def clean_restraunts_geo(rest_geo):
    rest_geo.dropna()
    rest_geo = rest_geo[rest_geo['Latitude']<41]
    rest_geo = rest_geo[rest_geo['Longitude']<-73.5]
    rest_geo = rest_geo[rest_geo['Longitude']>-75]

    return rest_geo