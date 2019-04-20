from flask import request
from flask_restful import Resource
from twitter import twitter_api
import tweepy
from models.collection import Collection


class TrendSearch(Resource):

    def post(self):

        mongo_hashtags = len(Collection.hashtags())
        if mongo_hashtags >= 10:
            return {"error": "MongoDB max capacity (10 already reached). Remove some Collections first:"}


        # Upload tweets to MongoDB
        mongodb = Collection()
        keyword = request.form.get('trend')

        if keyword[0] != '#':
            keyword = '#' + keyword
        count = int(request.form.get('count'))

        # Prevent overpopulating by deleting previously loaded tweets
        Collection.delete_by_hashtag(hashtag=keyword)

        for tweet in tweepy.Cursor(twitter_api.search, q=keyword).items(count):
            data = {}
            data['text'] = tweet.text
            data['hashtag'] = keyword
            data['created_at'] = tweet.created_at
            data['retweet_count'] = tweet.retweet_count
            try:
                mongodb.insert_data(data)
            except Exception as e:
                pass

        results = []
        for tweet in tweepy.Cursor(twitter_api.search, q=keyword).items(count):
            try:
                dict_ = {"user": tweet.user.name[:25],
                         "text": tweet.text,
                         "created_at": str(tweet.created_at),
                         "retweet_count": tweet.retweet_count,
                         "keyword": keyword
                         }
                results.append(dict_)
            except Exception as e:
                pass

        return results
