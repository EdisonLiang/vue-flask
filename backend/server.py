from flask import Flask, send_from_directory
import json

app = Flask(__name__)

@app.route("/api/dogs")
def get_dogs():
    dogs = [
        {
            'name': 'Keyton'
        },
        {
            'name': 'Troy'
        },
        {
            'name': 'Winna'
        },
        {
            'name': 'Star'
        }
    ]
    return json.dumps(dogs)


@app.route("/api/home")
def get_home():
    articles = [
        {'heading': 'hej', 'text': 'massa text', 'images': ['meh', 'muh']},
        {'heading': 'hej2', 'text': 'mera text', 'images': ['buh']}
    ]
    return json.dumps(articles)


@app.route("/")
def index():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()
