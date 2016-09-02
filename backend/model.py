# -*- coding: utf-8 -*-
from db import db
from sqlalchemy.dialects.postgresql import JSON
import datetime

class Home(db.Model):
    __tablename__ = 'home'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSON)
