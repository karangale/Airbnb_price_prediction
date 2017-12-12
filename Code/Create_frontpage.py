from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('new.html')

@app.route("/airbnb-restaurant", methods=['GET'])
def airbnb_restaurant():
    return render_template('airbnb-restaurant.html')

@app.route("/ML_model", methods=['POST'])
def ML_model():

    if request.method == 'POST':    
	    video_name = request.form['video_name']
	    channel_title = request.form['channel_title']
	    video_category = request.form['video_category']
	    description = request.form['description']

    print(video_name)
    if video_name is None:
        video_name = ""
    if channel_title is None:
        channel_title = ""
    if video_category is None:
        video_category = ""
    if description is None:
        description = ""

    recommend_tags = rec.initializeAndFetchRecommendations(video_name, channel_title, video_category, description)
    print("\n\n", recommend_tags)
    return render_template('ML_model.html', video_name = video_name, channel_title = channel_title, video_category = video_category, description = description, recommendation = recommend_tags)


if __name__=="__main__":
    app.run()

