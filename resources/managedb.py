from flask import Response, render_template, redirect, request
from flask_restful import Resource
from models.collection import Collection
from models.tweets import TweetsModel



class ManageDB(Resource):

    def get(self):
        ## MongoDB hashtags
        mongo_hashtags = Collection.hashtags()

        sqlite_hashtags = TweetsModel.distinct_hashtags()

        return Response(render_template("manage_db/manage_db.html", mongo_hashtags=mongo_hashtags,
                                        sqlite_hashtags=sqlite_hashtags))


class DeleteCollection(Resource):

    def post(self):
        hashtag = request.form.get('hashtag_collection')

        Collection.delete_by_hashtag(hashtag=hashtag)

        return redirect('managedb')


class DeleteTable(Resource):

    def post(self):
        hashtag = request.form.get('hashtag_table')
        TweetsModel.delete_by_hashtag(hashtag=hashtag)

        return redirect('managedb')
