from models.user import UserModel
from tests.base_test import BaseTest
from models.tweets import TweetsModel



class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'test@gmail.com','abcd')

            self.assertIsNone(UserModel.find_by_username('test'), "Found an user with name 'test' before save_to_db")
            self.assertIsNone(UserModel.find_by_id(1), "Found an user with id '1' before save_to_db")

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test'),
                                 "Did not find an user with name 'test' after save_to_db")
            self.assertIsNotNone(UserModel.find_by_id(1), "Did not find an user with id '1' after save_to_db")

            self.assertEqual(user.username, 'test',
                             "The name of the user after creation does not equal the constructor argument.")
            self.assertEqual(user.password, 'abcd',
                             "The password of the user after creation does not equal the constructor argument.")


class TweetTest(BaseTest):
    def test_crud(self):
        with self.app_context():

            tweet = TweetsModel('test', 'test')

            self.assertIsNone(TweetsModel.find_by_tweet('test'), "Found an tweet with name 'test' before save_to_db")

            tweet.save_to_db()

            self.assertIsNotNone(TweetsModel.find_by_tweet('test'),
                                 "Did not find an tweet with name 'test' after save_to_db")

            self.assertEqual(tweet.tweet, 'test',
                             "The name of the tweet after creation does not equal the constructor argument.")
            self.assertEqual(tweet.hashtag, 'test',
                             "The hashtag of the tweet after creation does not equal the constructor argument.")










