"""Machine learning model to predict airbnb prices."""
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn import linear_model
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import cleaning_utils
plt.style.use('ggplot')


ONE_HOT_ENCODE_COLUMNS = ["room_type", "bed_type", "cancellation_policy"]
BINARY_ENCODE_COLUMNS = ["host_has_profile_pic", "host_identity_verified",
                         "requires_license", "instant_bookable",
                         "is_business_travel_ready",
                         "require_guest_profile_picture",
                         "require_guest_phone_verification"]
LINEAR_REGRESSION_FEATURES = ['bedrooms', 'beds', 'accommodates', "rest_count",
                              'number_of_reviews', 'minimum_nights',
                              'maximum_nights']


def read_data(path, airbnb_file_name, restaurant_data_file_name):
    """
    Read the airbnb and restaurant data from the data directory.

    You must have listings.csv and rest_counts.csv files within the Data
    directory for this function to work.

    Args:
        path: (str) This is the path to the data file
    Returns:
        two dataframes, one with airbnb data and the other with the restaurant
        data
    """
    airbnb_data_file_path = os.path.join(path, 'Data', airbnb_file_name)
    restaurant_data_file_path = os.path.join(path, 'Data',
                                             restaurant_data_file_name)

    airbnb_data = pd.read_csv(airbnb_data_file_path, encoding='latin-1')
    restaurant_data = pd.read_csv(restaurant_data_file_path,
                                  encoding='latin-1')
    return airbnb_data, restaurant_data


def oneHotEncode(df, col_names):
    """
    Convert categorical variables into numerical features.

    This is done using the one hot encoding implementation within scikit-learn.
    It increases the number of features by the number of unique categories for
    the specified categorical variables ("room_type", "bed_type", and
    "cancellation_policy" in this case). It ensures no category gets more
    weightage than others after numerical representation. Particularly useful
    for features with more than two categories.

    Args:
        df: (dataframe) This is the dataframe on which the one hot encoding
        needs to be performed.
        col_names: (list) A list with the desired column names that need to be
        considered for one hot encoding
    Returns:
        a dataframe with additional features added for every category within
        columns specified in the col_names argument
    """
    enc = LabelEncoder()
    enc1 = OneHotEncoder()
    df_1 = pd.DataFrame()
    try:
        for col in col_names:
            if df[col].dtypes == 'object':
                df[col] = pd.Series(enc.fit_transform(df[[col]]),
                                    index=df.index)
                temp = enc1.fit(df[col].values)
                temp = pd.DataFrame(temp.toarray(),
                                    columns=[(col+"_"+str(i)) for
                                    i in df[col].value_counts().index])
                temp = temp.set_index(df.index.values)
                df_1 = pd.concat([df, temp], axis=1)
        return df_1
    except:
        print("Fail")
        return False


def binaryEncode(df, col_names):
    """
    Convert categorical variables into numerical features.

    This implementation is specifically for categorical variables with two
    categories. Does not add any new features for categories. Alters the
    existing column to a 0/1 representation for the two categories.

    Args:
        df: (dataframe) This is the dataframe on which binary encoding needs
        to be performed.
        col_names: (list) A list with the desired column names that need to be
        considered for binary encoding
    Returns:
        a dataframe with columns specified in the col_names argument as encoded
        as 0/1 for the two categories

    """
    for i in col_names:
        df[i] = df[i].apply(lambda x: 1 if x == 'y' else 0)

    return df


def build_linear_regression_model(feature_list):
    """
    Build the Linear Regression model used later for predicting listing prices.

    Only features of interest are used for building the model.
    The two data sets are joined on the id column and this dataset is used
    later for further analysis.

    Params:
        feature_list: (list) List of features used to build the Linear
        Regression model
    Returns:
        A model object with the data fit on the training data
    """
    try:
        current_dir_path = os.getcwd()
        airbnb_data_req, restaurant_data = read_data(current_dir_path,
                                                     'listings.csv',
                                                     'rest_count.csv')
        airbnb_data_req = binaryEncode(airbnb_data_req, BINARY_ENCODE_COLUMNS)
        airbnb_data_req = cleaning_utils.clean_airbnb(airbnb_data_req)

        # Merging the two datasets on id
        airbnb_data_req = airbnb_data_req.join(restaurant_data, on="id",
                                               how="inner")
        x_train = airbnb_data_req[feature_list]
        y_train = airbnb_data_req['price'].values

        reg = linear_model.LinearRegression()
        reg.fit(x_train, y_train)
        y_pred = reg.predict(x_train)
        print("Linear regression r squared", r2_score(y_train, y_pred), "\n")
        return reg
    except:
        return False


def predict_price(data):
    """
    Make predictions on the test data.

    It calls the build_linear_regression_model() function to build the linear
    regression model and makes the predictions for the data argument passed to
    the function as an argument.

    Params:
        data: (numpy array) An instance of data (with the features) for which
        the prediction has to be made
    Returns:
        A floating point number corresponding to the predicted value
    """
    model = build_linear_regression_model(LINEAR_REGRESSION_FEATURES)
    return model.predict(data)


if __name__ == '__main__':
    build_linear_regression_model(LINEAR_REGRESSION_FEATURES)
