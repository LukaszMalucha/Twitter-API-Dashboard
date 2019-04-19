from flask import request
from flask_restful import Resource
from twitter import twitter_api
import tweepy
from operator import itemgetter
import itertools

# City Trends Intersection

class CommonTrends(Resource):

    def post(self):

        city_1 = int(request.form.get('city_1'))
        city_2 = int(request.form.get('city_2'))

        try:
            city_1_trends = twitter_api.trends_place(city_1)
            city_2_trends = twitter_api.trends_place(city_2)

            city_1_trends_list = [(str(trend['name']), str(trend['tweet_volume'])) for trend in city_1_trends[0]['trends']]
            city_2_trends_list = [(str(trend['name']), str(trend['tweet_volume'])) for trend in city_2_trends[0]['trends']]

            city_intersection = [a for (a, b) in itertools.product(city_1_trends_list, city_2_trends_list) if a[:2] == b[:2]]

            clean_trends = []
            for trend in city_intersection:
                trend = [(trend[0]).replace('#', ''), (trend[1]).replace('None', '')]
                clean_trends.append(trend)

            return clean_trends

        except Exception as e:
            return {'error': 'Requested ID does not exist, try another one'}


class RetweetPopularity(Resource):
    """Retweet popularity search"""

    def post(self):
        keyword = request.form.get('keyword')
        count = int(request.form.get('count'))
        min_retweets = int(request.form.get('retweets'))
        counter = count * 4

        popular_tweets = []
        for tweet in tweepy.Cursor(twitter_api.search, q=keyword).items(counter):
            if tweet.retweet_count > min_retweets:
                dict_ = {"user": tweet.user.name[:25],
                         "text": tweet.text,
                         "created_at": str(tweet.created_at),
                         "retweet_count": tweet.retweet_count,
                         "keyword": keyword
                         }
                popular_tweets.append(dict_)

        tweets_list = popular_tweets[: count]
        tweets_sorted = sorted(tweets_list, key=itemgetter('retweet_count'), reverse=True)
        return tweets_sorted

        # IF PYTHON LIST NEEDED INSTEAD OF JSON:
        # results = [status._json for status in tweepy.Cursor(twitter_api.search, q=keyword, min_retweets=50).items(count)]
        # pop_tweets = [status
        #               for status in results
        #               if status._json['retweet_count'] > min_retweets]
        #
        # ## tuple of tweet + retweet count
        # tweet_list = [[tweet._json['text'], tweet._json['created_at'][:19], tweet._json['user']['name'],
        #                tweet._json['retweet_count']]
        #               for tweet in pop_tweets]
        # # tweet_list = {k: v  for v,k in enumerate(pop_tweets)}
        #
        #
        # ## sort descending
        # most_popular_tweets = sorted(tweet_list, key=itemgetter(3), reverse=True)[:count]

        # return Response(
        #     render_template("api_features/most_retweets.html", most_popular_tweets=most_popular_tweets, keyword=keyword,
        #                     count=count, min_retweets=min_retweets))

