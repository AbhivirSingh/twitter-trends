from flask import Flask, render_template, request
from script import collection, fetch_twitter_trends
from bson import json_util

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/results', methods=['GET'])
def results():
    trends = list(collection.find({}, {"_id": 0}))
    return json_util.dumps(trends)


@app.route('/run-script', methods=['POST'])
def run_script():
    request_data = request.get_json()
    example_value = request_data.get('cnt')
    data = fetch_twitter_trends(example_value)
    return json_util.dumps(data)


if __name__ == "__main__":
    app.run(debug=True)