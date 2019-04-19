## App Utilities
import os
import env
from db import db, mongo
from twitter import twitter_api

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_restful import Api
from flask_wtf.csrf import CSRFProtect

from models.collection import Collection
from models.tweets import TweetsModel

from resources.user import UserRegister, UserLogin, UserLogout, login_manager
from resources.blog_list import blog_list
from resources.api_features import CommonTrends, RetweetPopularity
from resources.managedb import DeleteCollection, DeleteTable, DataTransform
from resources.trend_search import TrendSearch
from resources.data_management import DataLoad
from resources.sentiment_analysis import SentimentAnalysis, TweetTokenizer, Results

# APP SETTINGS

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = True
api = Api(app)
mongo.init_app(app)
Bootstrap(app)
login_manager.init_app(app)

api.add_resource(DeleteCollection, '/deletecollection')
api.add_resource(DeleteTable, '/deletetable')
api.add_resource(CommonTrends, '/commontrends')
api.add_resource(RetweetPopularity, '/retweets')
api.add_resource(TrendSearch, '/trendsearch')
api.add_resource(DataTransform, '/datatransform')
api.add_resource(DataLoad, '/dataload')
api.add_resource(SentimentAnalysis, '/sentimentanalysis')
api.add_resource(TweetTokenizer, '/tweettokenizer')
api.add_resource(Results, '/results')

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')


## Main View
@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/trend_search')
def trend_search():
    """Trend Search View"""
    us_trends = twitter_api.trends_place(23424977)
    us_trends_list = [trend['name'] for trend in us_trends[0]['trends'][:40]]
    return render_template('trend_search/dashboard.html', us_trends_list=us_trends_list)


@app.route('/two_cities')
def two_cities():
    """Tale of Two Cities View"""
    return render_template('two_cities/dashboard.html')


@app.route('/popular_retweets')
def popular_retweets():
    """Tale of Two Cities View"""
    return render_template('popular_retweets/dashboard.html')


@app.route('/sentiment_analysis')
def sentiment_analysis():
    """Apply LSTM View"""
    return render_template('sentiment_analysis/dashboard.html')

@app.route('/manage_db')
def manage_db():
    """Manage Databases View"""
    mongo_hashtags = Collection.hashtags()
    sqlite_hashtags = TweetsModel.distinct_hashtags()
    return render_template('manage_db/dashboard.html', mongo_hashtags=mongo_hashtags, sqlite_hashtags=sqlite_hashtags)


@app.route('/blog')
def blog():
    """Blog"""
    blog_list.reverse()
    return render_template("blog.html", blog_list=blog_list)


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500


## DB INIT
db.init_app(app)
# csrf = CSRFProtect(app) @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

## APP INITIATION
if __name__ == '__main__':

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run()

# Docker
#     app.run(host='0.0.0.0')

# # Heroku
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
