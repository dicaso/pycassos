# -*- coding: utf-8 -*-
"""Users module

Flask functionality related to managing users and sessions.
"""
# prepare user database
from flask_mongoengine import MongoEngine
db = MongoEngine()

class User(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)

# login management
import flask_login as fl
login_manager = fl.LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
