from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('new.html')


@app.route("/airbnb-restaurant", methods=['GET'])
def airbnb_restaurant():
    return render_template('airbnb-restaurant.html')


@app.route("/get_model_page", methods=['GET'])
def get_model_page():
    return render_template('ML_model.html')


@app.route("/ML_model", methods=['GET', 'POST'])
def ML_model():
    
    if request.method == 'POST':    
        n_rooms = request.form['n_rooms']
        nbeds = request.form['nbeds']
        naccommodates = request.form['naccommodates']
        nrestaurants = request.form['nrestaurants']
        nreviews = request.form['nreviews']
        nrating = request.form['nrating']
        region = request.form['region']

    if n_rooms is None:
        n_rooms = ""
    if nbeds is None:
        nbeds = ""
    if naccommodates is None:
        naccommodates = ""
    if nrestaurants is None:
        nrestaurants = ""
    if nreviews is None:
        nreviews = ""
    if nrating is None:
        nrating = ""
    if region is None:
        region = ""

    prediction = "prediction"
    print(region)

    return render_template('ML_model.html', n_rooms = n_rooms, nbeds = nbeds, naccommodates = naccommodates, 
                                            nrestaurants = nrestaurants,  nreviews = nreviews, nrating = nrating, 
                                            region = region, prediction = prediction)


if __name__=="__main__":
    app.run()

