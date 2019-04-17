from flask import session, Response, render_template, redirect
from flask_restful import Resource
from models.collection import Collection
from models.tweets import TweetsModel

# getting the root of every word (stemming):
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
import re
from models.stopwords import stopwords  # get rid of irrelevant and stemming words


class DataTransform(Resource):

    def get(self):

        return redirect('trendsearch')

    def post(self):

        hashtag = session.get('hashtag')

        if hashtag is None:
            return redirect('trendsearch', message="hashtag was not specified")

        ## Get chosen hashtag tweets
        hashtag_tweets = Collection.find_by_hashtag(hashtag=hashtag)

        ## Preprocess text for future senitment analysis
        text = [element['text'] for element in hashtag_tweets]

        corpus = []
        for i in range(0, len(text)):
            tweet = re.sub('[^a-zA-Z]', ' ', text[i])  ## all the indexes
            tweet = tweet.lower()
            tweet = tweet.split()
            ps = PorterStemmer()
            tweet = [ps.stem(word) for word in tweet if not word in stopwords]
            tweet = ' '.join(tweet)
            corpus.append(tweet)
            new_tweet = TweetsModel(hashtag=hashtag, tweet=tweet)
            new_tweet.save_to_db()

        return Response(
            render_template("data_management/data_transform.html", text=text, corpus=corpus, hashtag=hashtag))


class DataLoad(Resource):

    def get(self):
        hashtag = session.get('hashtag')

        hashtag_tweets = TweetsModel.find_by_hashtag(hashtag=hashtag)

        return Response(
            render_template("data_management/data_load.html", hashtag_tweets=hashtag_tweets, hashtag=hashtag))
