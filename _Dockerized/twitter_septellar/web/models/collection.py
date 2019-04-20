from db import mongo


class Collection():

    def __init__(self):
        self.mongo = mongo

    def insert_data(self, data):
        return mongo.db.harvest_tweets.insert(data)

    @classmethod
    def hashtags(cls):
        return mongo.db.harvest_tweets.distinct("hashtag")

    @classmethod
    def find_by_hashtag(cls, hashtag):
        return mongo.db.harvest_tweets.find({"hashtag": hashtag})

    @classmethod
    def delete_by_hashtag(cls, hashtag):
        return mongo.db.harvest_tweets.remove({"hashtag": hashtag})
