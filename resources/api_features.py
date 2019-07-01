from flask import request
from flask_restful import Resource
from twitter import twitter_api
import tweepy
from operator import itemgetter
import itertools

# City Trends Intersection

# QUICKFIX
trends_list = [["Mother's Day", "1124741"], ["MothersDay", "591302"], ["Moms", "536456"], ["Happy Mothers", "276271"],
            ["IPL2019Final", "126930"], ["HappyMothersDay2019", "111327"], ["Porzingis", "112398"],
            ["Doris Day", "108480"], ["lotteryseatupgrade", "33000"], ["Brault", "15000"]]

class CommonTrends(Resource):

    def post(self):

        # city_1 = int(request.form.get('city_1'))
        # city_2 = int(request.form.get('city_2'))
        #
        try:
        #     city_1_trends = twitter_api.trends_place(city_1)
        #     city_2_trends = twitter_api.trends_place(city_2)
        #
        #     city_1_trends_list = [(str(trend['name']), str(trend['tweet_volume'])) for trend in city_1_trends[0]['trends']]
        #     city_2_trends_list = [(str(trend['name']), str(trend['tweet_volume'])) for trend in city_2_trends[0]['trends']]
        #
        #     city_intersection = [a for (a, b) in itertools.product(city_1_trends_list, city_2_trends_list) if a[:2] == b[:2]]
        #
        #     clean_trends = []
        #     for trend in city_intersection:
        #         trend = [(trend[0]).replace('#', '')[:27], (trend[1]).replace('None', '< 10000'), (trend[0]).replace('#', '%23')]
        #         clean_trends.append(trend)
            clean_trends = trends_list
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

