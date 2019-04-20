from flask import Response, render_template, request, session
from flask_restful import Resource

from models.tweets import TweetsModel
from models.collection import Collection

import pickle
from keras.preprocessing.sequence import pad_sequences
from keras import backend as K
from sentiment_model.load import init_model
import numpy as np

import os.path

# PATHS
my_path = os.path.abspath(os.path.dirname(__file__))
tokenizer_path = os.path.join(my_path, "../sentiment_model/tokenizer.pickle")


class TweetTokenizer(Resource):

    def post(self):
        hashtag = request.form.get('hashtag')

        # for backend sentiment analysis
        hashtag_tweets = TweetsModel.find_by_hashtag(hashtag=hashtag)
        hashtag_tweets = [element.tweet for element in hashtag_tweets]

        # load pickled tokenizer
        with open(tokenizer_path, 'rb') as handle:
            tokenizer = pickle.load(handle)

        # preprocess data for prediction
        tokenized = []
        for element in hashtag_tweets:
            element = element.split()
            element = tokenizer.texts_to_sequences(element)
            tokenized.append(element)
        session['tokenized'] = tokenized
        session['hashtag'] = hashtag
        return hashtag


class Results(Resource):

    def post(self):

        K.clear_session()
        model, graph = init_model()
        hashtag = session.get('hashtag')
        tokenized = session.get('tokenized')

        # for table display
        tweets = Collection.find_by_hashtag(hashtag=hashtag)
        tweets = [element['text'] for element in tweets]

        # apply model
        predictions = []
        with graph.as_default():
            for element in tokenized:
                element = pad_sequences(element, maxlen=23, dtype='int32', value=0)
                prediction = model.predict(element, batch_size=1, verbose=2)[0]
                if (np.argmax(prediction) == 0):
                    prediction = 'Negative'
                elif (np.argmax(prediction) == 1):
                    prediction = 'Neutral'
                else:
                    prediction = 'Positive'
                predictions.append(prediction)

        # zip predictions with ORIGINAL tweet for better clarity
        sentiment_predictions = list(zip(tweets, predictions))

        return sentiment_predictions
