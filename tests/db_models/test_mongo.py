from tests.base_test import BaseTest
from app import mongo



class CollectionTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            test_collection = {"hashtag": "test", "tweet": "test"}
            tests = mongo.db.tests
            self.assertEqual(mongo.db.tests.find({"algorithm": "test"}).count(), 0,
                             "Found a tweet in mongo database, but expected not to")

            tests.insert_one(test_collection)

            self.assertIsNotNone(mongo.db.tests.find({"tweet": "test"}),
                             "Tweet was not saved to mongodb")

            mongo.db.tests.remove({"tweet": "test"})

            self.assertEqual(mongo.db.tests.find({"tweet": "test"}).count(), 0,
                             "Found a tweet in mongo database, but expected not to")


