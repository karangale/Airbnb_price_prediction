def splitZip(zipcode):
    zips = zipcode.split("-")
    zipsDot = zips[0].split(".")
    zipsN = zipsDot[0].split("\n")
    return zipsN[0]

def rest_name(restaurants):
    i = len(restaurants)
    restaurant = restaurants[:(i-6)]
    length = len(restaurant)
    num = ['0','1','2','3','4','5','6','7','8','9','-', '.']
    for j in range((length-1),0,-1):
        if(restaurant[j] in num):
            if((restaurant[j-1]==" ")and(restaurant[j-2] not in num)):
                break;
            else:
                continue

    name = restaurant[:(j-1)]

    if(name==""):
        name = restaurants[:len(restaurants)-17]

    return name

def rest_add(row):
    add = row['Restaurant'].split(row['Name'])[1]
    return add

def clean_airbnb(airbnb_data_req):
    columns_interest_airbnb = ['street', 'neighbourhood','zipcode', 'latitude', 'longitude', 'property_type', 'accommodates',
                               'bathrooms', 'bedrooms', 'beds', 'price', 'minimum_nights', 'maximum_nights',
                               'number_of_reviews', 'neighbourhood_group_cleansed', 'review_scores_rating', 'picture_url']
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
    airbnb_data_req = airbnb_data_req[airbnb_data_req['zipcode']!='1m']

    airbnb_data_req = airbnb_data_req[airbnb_data_req['property_type'] == 'Apartment']

    airbnb_data_req['review_scores_rating'].dropna().reset_index()

    return airbnb_data_req

def clean_airbnb_map(airbnb_data_req):
    columns_interest_airbnb = ['host_name', 'street', 'neighbourhood', 'zipcode', 'latitude', 'longitude', 'property_type', 'accommodates',
                               'bathrooms', 'bedrooms', 'beds', 'price',
                               'number_of_reviews', 'neighbourhood_group_cleansed', 'review_scores_rating', 'picture_url', 'listing_url']
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
    airbnb_data_req = airbnb_data_req[airbnb_data_req['zipcode']!='1m']

    airbnb_data_req = airbnb_data_req[airbnb_data_req['property_type'] == 'Apartment']

    airbnb_data_req['review_scores_rating'].dropna().reset_index()

    return airbnb_data_req

def clean_restraunts_geo(rest_geo):
    rest_geo.dropna()
    rest_geo = rest_geo[rest_geo['Latitude']<41]
    rest_geo = rest_geo[rest_geo['Longitude']<-73.5]
    rest_geo = rest_geo[rest_geo['Longitude']>-75]

    rest_geo['Name'] = rest_geo['Restaurant'].apply(rest_name)
    rest_geo['Address'] = rest_geo.apply(rest_add,axis=1)

    return rest_geo
