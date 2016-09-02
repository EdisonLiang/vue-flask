# -*- coding: utf-8 -*-
from flask import Flask, send_from_directory

from db import db
from model import Home
from transaction import transaction_wrapper

import json
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/api/home")
@transaction_wrapper
def get_home():
    articles = Home.query.with_entities(Home.data).all()
    return json.dumps([article.data for article in articles])

@app.route("/")
def index():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()
