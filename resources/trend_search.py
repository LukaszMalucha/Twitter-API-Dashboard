from flask import session, Response, render_template, request
from flask_restful import Resource
from twitter import twitter_api
import tweepy
from models.collection import Collection


################################################################### Trend Search


class TrendSearch(Resource):

    def get(self):

        ## Get US most trending
        us_trends = twitter_api.trends_place(23424977)
        us_trends_list = [trend['name'] for trend in us_trends[0]['trends'][:40]]

        return Response(render_template("trend_search/trend_search.html", us_trends_list=us_trends_list))

    def post(self):

        ## Upload tweets to MongoDB
        mongodb = Collection()
        keyword = request.form.get('trend')
        if keyword[0] != '#':
            keyword = '#' + keyword
        count = int(request.form.get('count'))

        for tweet in tweepy.Cursor(twitter_api.search, q=keyword).items(count):
            data = {}
            data['text'] = tweet.text
            data['hashtag'] = keyword
            data['created_at'] = tweet.created_at
            data['retweet_count'] = tweet.retweet_count
            try:
                mongodb.insert_data(data)
            except:
                pass

        results = [status for status in tweepy.Cursor(twitter_api.search, q=keyword).items(count)]

        ## Display tweets
        tweet_list = [[tweet._json['text'], tweet._json['created_at'][:19], tweet._json['user']['name'],
                       tweet._json['retweet_count']]
                      for tweet in results]

        session['hashtag'] = keyword

        return Response(render_template("trend_search/tweets.html", tweet_list=tweet_list, keyword=keyword))
