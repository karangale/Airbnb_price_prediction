"""File containing cleaning functions for the datasets."""
LATITUDE = 41
LONGITUDE_LOWER = -75
LONGITUDE_UPPER = -73.5
NUM_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.']


def splitZip(zipcode):
    """
    Remove the special characters present in the zip codes.

    Args:
        zipcode: (alphanumeric) The zipcode which needs to be processed to
        conform to a standard format
    Returns:
        The zipcode after removing special characters
    """
    zips = zipcode.split("-")
    zipsDot = zips[0].split(".")
    zipsN = zipsDot[0].split("\n")
    return zipsN[0]


def clean_airbnb(airbnb_data_req):
    """
    Clean up the airbnb data.

    It handles multiple use cases like null handling,
    imputing empty cell data etc.
    It also removes rows for which there is skewed representation in the data.
    Removes the special characters from amount fields.

    Args:
        airbnb_data_req: (dataframe) The dataframe that needs to be cleaned
    Returns:
        A dataframe after the cleaning has been performed.
    """
    index_drop = airbnb_data_req[airbnb_data_req['zipcode'].
                                 isnull()].index.tolist()
    airbnb_data_req = airbnb_data_req.drop(index_drop)
    airbnb_data_req = airbnb_data_req.reset_index(drop=True)

    airbnb_data_req["bathrooms"].fillna(0, inplace=True)
    airbnb_data_req["bedrooms"].fillna(0, inplace=True)
    airbnb_data_req["beds"].fillna(0, inplace=True)
    airbnb_data_req["neighbourhood"].fillna("", inplace=True)

    airbnb_data_req["price"] = airbnb_data_req["price"].str.replace('$', '')
    airbnb_data_req["price"] = airbnb_data_req["price"].str.replace(',', '')
    airbnb_data_req["price"] = airbnb_data_req["price"].astype(float)

    airbnb_data_req["cleaning_fee"] = airbnb_data_req["cleaning_\
                                        fee"].str.replace('$', '')
    airbnb_data_req["cleaning_fee"] = airbnb_data_req["cleaning_\
                                        fee"].str.replace(',', '')
    airbnb_data_req["cleaning_fee"] = airbnb_data_req["cleaning_\
                                        fee"].astype(float)

    airbnb_data_req["extra_people"] = airbnb_data_req["extra_\
                                        people"].str.replace('$', '')
    airbnb_data_req["extra_people"] = airbnb_data_req["extra_\
                                        people"].str.replace(',', '')
    airbnb_data_req["extra_people"] = airbnb_data_req["extra_\
                                        people"].astype(float)

    airbnb_data_req["zipcode"] = airbnb_data_req["zipcode"].astype(str)

    airbnb_data_req["zipcode"] = airbnb_data_req["zipcode"].apply(splitZip)
    airbnb_data_req = airbnb_data_req[airbnb_data_req['zipcode'] != '1m']

    airbnb_data_req = airbnb_data_req[airbnb_data_req['property_\
                                        type'] == 'Apartment']
    airbnb_data_req = airbnb_data_req[airbnb_data_req['country_code'] == "US"]

    return airbnb_data_req


def rest_name(rest_name):
    """
    Check if the restaurant name exists.

    Args:
        row_data: (dataframe row) A row of the restaurant data
    Returns:
        A row with the transformed data
    """
    i = len(rest_name)
    restaurant = rest_name[:(i-6)]
    length = len(restaurant)
    for j in range((length-1), 0, -1):
        if(restaurant[j] in NUM_LIST):
            if((restaurant[j-1] == " ")and(restaurant[j-2] not in NUM_LIST)):
                break
            else:
                continue

    name = restaurant[:(j-1)]

    if(name == ""):
        name = rest_name[:len(rest_name)-17]

    return name


def rest_add(row_data):
    """
    Apply a row level transformation to the to return the restaurant name.

    Args:
        row_data: (dataframe row) A row of the restaurant data
    Returns:
        A row with the transformed data
    """
    add = row_data['Restaurant'].split(row_data['Name'])[1]
    return add


def clean_restraunts_geo(restaurant_data):
    """
    Limit the geography of the data to around New York.

    Args:
        restaurant_data: (dataframe) The restaurant dataframe to be cleaned
    Returns:
        The cleaned restaurant dataframe
    """
    restaurant_data.dropna()
    restaurant_data = restaurant_data[restaurant_data['Latitude'] < LATITUDE]
    restaurant_data = restaurant_data[restaurant_data['Longitude'] >
                                      LONGITUDE_LOWER]
    restaurant_data = restaurant_data[restaurant_data['Longitude'] <
                                      LONGITUDE_UPPER]

    restaurant_data['Name'] = restaurant_data['Restaurant'].apply(rest_name)
    restaurant_data['Address'] = restaurant_data.apply(rest_add, axis=1)

    return restaurant_data
