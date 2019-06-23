from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from pymongo.errors import AutoReconnect


db = SQLAlchemy()
mongo = PyMongo()
