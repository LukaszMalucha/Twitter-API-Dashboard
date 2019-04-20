from db import db


class TweetsModel(db.Model):
    __tablename__ = 'tweets'
    id = db.Column('id', db.Integer, primary_key=True)
    hashtag = db.Column('hashtag', db.Unicode)
    tweet = db.Column('tweet', db.Unicode)

    def __init__(self, hashtag, tweet):
        self.hashtag = hashtag
        self.tweet = tweet

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def distinct_hashtags(self):
        return db.session.query(self.hashtag.distinct())

    @classmethod
    def delete_by_hashtag(cls, hashtag):
        tweets = cls.query.filter_by(hashtag=hashtag).delete()
        db.session.commit()

    @classmethod
    def find_by_hashtag(cls, hashtag):
        return cls.query.filter_by(hashtag=hashtag).all()

    @classmethod
    def find_by_tweet(cls, tweet):
        return cls.query.filter_by(tweet=tweet).first()
