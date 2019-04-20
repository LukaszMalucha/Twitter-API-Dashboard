from flask import redirect, request
from flask_restful import Resource
from models.collection import Collection
from models.tweets import TweetsModel

# getting the root of every word (stemming):
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
import re

from models.stopwords import stopwords  # get rid of irrelevant and stemming words


class DeleteCollection(Resource):

    def post(self):
        hashtag = request.form.get('hashtag_collection')
        Collection.delete_by_hashtag(hashtag=hashtag)
        return redirect('manage_db')


class DeleteTable(Resource):

    def post(self):
        hashtag = request.form.get('hashtag_table')
        TweetsModel.delete_by_hashtag(hashtag=hashtag)
        return redirect('manage_db')


class DataTransform(Resource):

    def post(self):

        hashtag = request.form.get('hashtag_cleaning')

        # Prevent overpopulating
        TweetsModel.delete_by_hashtag(hashtag=hashtag)

        if hashtag is None:
            return redirect('trendsearch', message="hashtag was not specified")

        # Get chosen hashtag tweets
        hashtag_tweets = Collection.find_by_hashtag(hashtag=hashtag)

        # Preprocess text for future senitment analysis
        text = [element['text'] for element in hashtag_tweets]

        corpus = []
        for i in range(0, len(text)):
            try:
                tweet = re.sub('[^a-zA-Z]', ' ', text[i])  ## all the indexes
                tweet = tweet.lower()
                tweet = tweet.split()
                ps = PorterStemmer()
                tweet = [ps.stem(word) for word in tweet if not word in stopwords]
                tweet = ' '.join(tweet)
                corpus.append(tweet)
                new_tweet = TweetsModel(hashtag=hashtag, tweet=tweet)
                new_tweet.save_to_db()
            except Exception as e:
                pass


        return redirect('manage_db')