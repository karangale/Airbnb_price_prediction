import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import r2_score
from sklearn import linear_model
from sklearn.linear_model import ElasticNet
import geopy
from geopy.distance import vincenty
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
plt.style.use('ggplot')


airbnb_data = pd.read_csv("listings.csv", encoding='latin-1')


column_names = ["id", "host_listings_count", "host_total_listings_count", "host_has_profile_pic", "host_identity_verified", 
            "street", "neighbourhood", "city", "state", "zipcode", "market", "country_code", "country", "latitude", "longitude", "property_type",
             "room_type", "accommodates", "bathrooms", "bedrooms", "beds", "bed_type", "price", "cleaning_fee", "extra_people", "requires_license",
             "minimum_nights", "maximum_nights",  "has_availability", "availability_30", "availability_60", "number_of_reviews", "review_scores_value", 
             "instant_bookable", "is_business_travel_ready", "cancellation_policy", "require_guest_profile_picture", "require_guest_phone_verification", 
             "calculated_host_listings_count", "reviews_per_month"]


columns_interest_airbnb = ['street', 'neighbourhood','zipcode', 'latitude', 'longitude', 'property_type', 'accommodates', 
                               'bathrooms', 'bedrooms', 'beds', 'price', 'minimum_nights', 'maximum_nights', 
                               'number_of_reviews']

airbnb_data_req = airbnb_data[column_names]



prop_type= airbnb_data_req.groupby('property_type')['property_type'].count()
# prop_type.plot(kind='bar',figsize=(14,6))
# plt.show()

#Thus, as the distribution is skewed, we will only be using the property-type with entries as 'apartment'

def oneHotEnconde(df):
    enc = LabelEncoder()
    enc1 = OneHotEncoder()
    df_1=pd.DataFrame()

    for col in ["room_type", "bed_type", "cancellation_policy"]:
        # df[col] = df[col].astype(str)
        if df[col].dtypes == 'object':
            # enc.fit(df[[col]].values)
            df[col] =  pd.Series(enc.fit_transform(df[[col]]), index=df.index)
            # print("\n\n", type(enc.fit_transform(df[[col]])), "\n\n")
            temp = enc1.fit(df[col].values)
            temp = pd.DataFrame(temp.toarray(), columns=[(col+"_"+str(i)) for i in df[col].value_counts().index])
            temp = temp.set_index(df.index.values)
            df_1 = pd.concat([df, temp],axis=1)
    return df_1


def binaryEncode(df):

    cols = ["host_has_profile_pic", "host_identity_verified", "requires_license", "instant_bookable", "is_business_travel_ready", 
            "require_guest_profile_picture", "require_guest_phone_verification"]
    for i in cols:
        df[i] = df[i].apply(lambda x: 1 if x =='y' else 0)
    return df


def splitZip(zipcode):
    zips = zipcode.split("-")
    zipsDot = zips[0].split(".")
    zipsN = zipsDot[0].split("\n")
    return zipsN[0]


def clean_airbnb(airbnb_data_req):
    index_drop = airbnb_data_req[airbnb_data_req['zipcode'].isnull()].index.tolist()
    airbnb_data_req = airbnb_data_req.drop(index_drop)
    airbnb_data_req = airbnb_data_req.reset_index(drop = True)
    
    airbnb_data_req["bathrooms"].fillna(0, inplace = True)
    airbnb_data_req["bedrooms"].fillna(0, inplace = True)
    airbnb_data_req["beds"].fillna(0, inplace = True)
    airbnb_data_req["neighbourhood"].fillna("", inplace = True)
    airbnb_data_req["bathrooms"].fillna(0, inplace = True)
    
    airbnb_data_req["price"] = airbnb_data_req["price"].str.replace('$', '')
    airbnb_data_req["price"] = airbnb_data_req["price"].str.replace(',', '')
    airbnb_data_req["price"] = airbnb_data_req["price"].astype(float)
    
    airbnb_data_req["cleaning_fee"] = airbnb_data_req["cleaning_fee"].str.replace('$', '')
    airbnb_data_req["cleaning_fee"] = airbnb_data_req["cleaning_fee"].str.replace(',', '')
    airbnb_data_req["cleaning_fee"] = airbnb_data_req["cleaning_fee"].astype(float)

    airbnb_data_req["extra_people"] = airbnb_data_req["extra_people"].str.replace('$', '')
    airbnb_data_req["extra_people"] = airbnb_data_req["extra_people"].str.replace(',', '')
    airbnb_data_req["extra_people"] = airbnb_data_req["extra_people"].astype(float)

    airbnb_data_req["zipcode"] = airbnb_data_req["zipcode"].astype(str)
    
    airbnb_data_req["zipcode"] = airbnb_data_req["zipcode"].apply(splitZip)
    airbnb_data_req= airbnb_data_req[airbnb_data_req['zipcode']!='1m']
    
    airbnb_data_req = airbnb_data_req[airbnb_data_req['property_type'] == 'Apartment']
    airbnb_data_req = airbnb_data_req[airbnb_data_req['country_code']=="US"]

    return airbnb_data_req


airbnb_data_req = binaryEncode(airbnb_data_req)
# airbnb_data_req = oneHotEnconde(airbnb_data_req)
airbnb_data_req = clean_airbnb(airbnb_data_req)

print(airbnb_data_req.columns)

grouped_zipcode = airbnb_data_req.groupby('zipcode')

    x_train = airbnb_data_req[['bedrooms','bathrooms','accommodates','beds','number_of_reviews', 'minimum_nights', 'maximum_nights', 'number_of_reviews', "host_has_profile_pic", "host_identity_verified", "requires_license", "instant_bookable", "is_business_travel_ready", "require_guest_profile_picture", "require_guest_phone_verification"]]

y_train = airbnb_data_req['price'].values


reg=linear_model.LinearRegression()
reg.fit(x_train, y_train)
y_pred = reg.predict(x_train)
print("Linear regression r squared", r2_score(y_train,y_pred), "\n")


reg1=ElasticNet()
reg1.fit(x_train, y_train)
y_pred1 = reg1.predict(x_train)
print("Elastic regression r squared", r2_score(y_train, y_pred1), "\n")


reg2=linear_model.Lasso(alpha=.16)
reg2.fit(x_train, y_train)
y_pred2 = reg2.predict(x_train)
print("Lasso regression r squared", r2_score(y_train, y_pred1), "\n")

# coords_1 = (52.2296756, 21.0122287)
# coords_2 = (52.406374, 16.9251681)

# geopy.distance.vincenty(coords_1, coords_2).km