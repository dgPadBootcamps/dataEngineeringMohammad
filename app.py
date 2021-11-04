from flask import Flask, jsonify
from Test import tw

app = Flask(__name__)


@app.route('/')
def tweets():
    return jsonify(tw())


app.run(debug=True)
