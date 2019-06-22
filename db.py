from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from pymongo.errors import AutoReconnect


db = SQLAlchemy()
mongo = PyMongo()

# Handling AutoReconnect Error
def autoreconnect_retry(retries=3):
    def autoreconnect_retry_decorator(fn):
        def db_op_wrapper(*args, **kwargs):
            tries = 0

            while tries < retries:
                try:
                    return fn(*args, **kwargs)

                except AutoReconnect:
                    tries += 1

            raise Exception("No luck even after %d retries" % retries)

        return db_op_wrapper
    return autoreconnect_retry_decorator