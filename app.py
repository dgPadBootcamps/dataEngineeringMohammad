import json

from flask import Flask, jsonify, render_template
from data_collection.collection import search
from data_collection.get_hashtags import get_hashtags
from datetime import datetime, timedelta

today = datetime.utcnow().date()  # to concatenate in the file name the date of today
yesterday = today - timedelta(days=1)

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello"


@app.route('/tweets/<tweet>')
def tweets(tweet):
    return jsonify(search(tweet, yesterday, today))


@app.route('/twitter/taganalysis/<word>')
def top_hashtags(word):
    return jsonify(get_hashtags(word))


app.run(debug=True)
