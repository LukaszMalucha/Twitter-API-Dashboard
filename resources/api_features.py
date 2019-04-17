from flask import session, Response, render_template, redirect, request
from flask_restful import Resource
from twitter import twitter_api
import tweepy
from operator import itemgetter


########################################## City Trends Intersection

class CommonTrends(Resource):

    def get(self):
        return Response(render_template('api_features/twitter_trends.html'))

    def post(self):

        city_1 = int(request.form.get('city_1'))
        city_2 = int(request.form.get('city_2'))

        try:
            city_1_trends = twitter_api.trends_place(city_1)
            city_2_trends = twitter_api.trends_place(city_2)

            if city_1_trends and city_2_trends:
                city_1_trends_set = set([trend['name'] for trend in city_1_trends[0]['trends']])
                city_2_trends_set = set([trend['name'] for trend in city_2_trends[0]['trends']])
            #
            # find out common trends
            common_trends = set.intersection(city_1_trends_set, city_2_trends_set)

            clean_trends = set()
            for trend in common_trends:
                trend = trend.replace('#', '')
                clean_trends.add(trend)

            return Response(render_template("api_features/common_trends.html", clean_trends=clean_trends))

        except:

            return Response(render_template("api_features/twitter_trends.html",
                                            message="Requested ID does not exist, try another one:"))


################################################ Retweet popularity


class RetweetPopularity(Resource):

    def get(self):
        return Response(render_template('api_features/retweet_popularity.html'))

    def post(self):
        keyword = request.form.get('keyword')
        count = int(request.form.get('count'))
        min_retweets = int(request.form.get('retweets'))

        ## get tweets for the search query

        results = [status for status in tweepy.Cursor(twitter_api.search, q=keyword).items(count)]

        pop_tweets = [status
                      for status in results
                      if status._json['retweet_count'] > min_retweets]

        ## tuple of tweet + retweet count
        tweet_list = [[tweet._json['text'], tweet._json['created_at'][:19], tweet._json['user']['name'],
                       tweet._json['retweet_count']]
                      for tweet in pop_tweets]

        ## sort descending
        most_popular_tweets = sorted(tweet_list, key=itemgetter(3), reverse=True)[:count]

        return Response(
            render_template("api_features/most_retweets.html", most_popular_tweets=most_popular_tweets, keyword=keyword,
                            count=count, min_retweets=min_retweets))
