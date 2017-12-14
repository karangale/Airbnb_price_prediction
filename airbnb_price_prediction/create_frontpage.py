"""Create and run the web page to see the model and visualization."""
from flask import Flask, render_template, request
import ml_model as model
import numpy as np
import math
app = Flask(__name__)


@app.route("/")
def main():
    """
    Direct user to the homepage.

    This is a GET request by default.
    """
    return render_template('new.html')


@app.route("/airbnb_restaurant", methods=['GET'])
def airbnb_restaurant():
    """
    Direct user to restaurant visualization.

    This is a GET request.
    """
    return render_template('airbnb_restaurant.html')


@app.route("/get_model_page", methods=['GET'])
def get_model_page():
    """
    Direct user to the ML price prediction visualization.

    This is a GET request.
    """
    return render_template('ML_model.html')


@app.route("/ML_model", methods=['GET', 'POST'])
def render_prediction_module():
    """
    Direct to the ML price prediction visualization with the predicted value.

    This is a POST request.
    """
    if request.method == 'POST':
        n_rooms = request.form['n_rooms']
        nbeds = request.form['nbeds']
        naccommodates = request.form['naccommodates']
        nrestaurants = request.form['nrestaurants']
        nreviews = request.form['nreviews']
        nrating = request.form['nrating']
        min_nights = request.form['min_nights']
        max_nights = request.form['max_nights']

        if(n_rooms == "" or n_rooms is None):
            n_rooms = 0.0
        else:
            n_rooms = float(n_rooms)

        if(nbeds == "" or nbeds is None):
            nbeds = 0.0
        else:
            nbeds = float(nbeds)

        if(naccommodates == "" or naccommodates is None):
            naccommodates = 0.0
        else:
            naccommodates = float(naccommodates)

        if(nrestaurants == "" or nrestaurants is None):
            nrestaurants = 0.0
        else:
            nrestaurants = float(nrestaurants)

        if(nreviews == "" or nreviews is None):
            nreviews = 0.0
        else:
            nreviews = float(nreviews)

        if(nrating == "" or nrating is None):
            nrating = 0.0
        else:
            nrating = float(nrating)

        if(min_nights == "" or min_nights is None):
            min_nights = 0.0
        else:
            min_nights = float(min_nights)

        if(max_nights == "" or max_nights is None):
            max_nights = 0.0
        else:
            max_nights = float(max_nights)

    prediction = model.predict_price(np.array([[n_rooms, nbeds, naccommodates,
                                     nrestaurants, nreviews, min_nights,
                                     max_nights]]))
    prediction_final = prediction[0]
    prediction_final = math.ceil(prediction_final*100)/100
    return render_template('ML_model.html', n_rooms=n_rooms,
                           nbeds=nbeds, naccommodates=naccommodates,
                           nrestaurants=nrestaurants,  nreviews=nreviews,
                           nrating=nrating, min_nights=min_nights,
                           max_nights=max_nights, prediction=prediction_final)

def main():
    app.run()
