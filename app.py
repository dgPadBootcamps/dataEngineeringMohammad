from flask import Flask, jsonify
from Test import read_tweets
from Test import save_tweets

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello"


@app.route('/tweets/<search>')
def tweets(search):
    return jsonify(read_tweets(search))


@app.route('/save/<search>')
def save(search):
    return jsonify(save_tweets(search))


app.run(debug=True)
