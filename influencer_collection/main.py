from flask import Flask, jsonify
from datetime import datetime, timedelta
from flask import render_template
#
# from influencer_collection.
# from influencer_collection.influencer import get_influencers
# from influencer_collection.topics import get_topics
import topics
import influencer
import dataRead

today = datetime.utcnow().date()  # to concatenate in the file name the date of today
yesterday = today - timedelta(days=1)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/influencers_analysis')
def top_influencers_analysis():
    data = dataRead.read_data()
    influencers = influencer.get_influencers(data)
    influencers_topic = topics.get_topics(influencers)
    response = jsonify(influencers_topic)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
