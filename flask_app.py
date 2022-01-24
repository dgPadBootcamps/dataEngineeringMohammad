import json
from flask import Flask, jsonify
from data_collection.collection import search
from datetime import datetime, timedelta
from flask import render_template

from influencer_collection.dataRead import read_data
from influencer_collection.influencer import get_influencers
from influencer_collection.topics import get_topics

today = datetime.utcnow().date()  # to concatenate in the file name the date of today
yesterday = today - timedelta(days=1)

app = Flask(__name__)




@app.route("/")
def index():
    return 'hello'


@app.route('/tweets/<tweet>')
def tweets(tweet):
    return jsonify(search(tweet, yesterday, today))


@app.route('/hashtags')
def top_hashtags():
    file_path = "C:/Users/MOHD/Documents/dgPad/dgPad2/hashtags_collection/hashtags.json"
    with open(file_path, 'r', encoding="utf8") as hashtags:
        data = json.loads(hashtags.read())
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/influencers')
def top_influencers():
    file_path = "C:/Users/MOHD/Documents/dgPad/dgPad2/influencer_collection/influencers_topics.json"
    with open(file_path, 'r', encoding="utf8") as hashtags:
        data = json.loads(hashtags.read())
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/influencers_analysis')
def top_influencers_analysis():
    data = read_data()
    influencers = get_influencers(data)
    influencers_topic = get_topics(influencers)
    response = jsonify(influencers_topic)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
