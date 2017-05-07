from hamcrest import *
from mock import MagicMock

from app.twitter_bot import TwitterBot


class TestTwitterBot():
    def setUp(self):
        self.api = MagicMock()
        self.twitter_bot = TwitterBot(api=self.api)

    def test_get_text_none(self):
        self.setUp()
        text = self.twitter_bot.get_basic_text(text=None)
        expected_text = 'Hello World!'
        assert_that(text, equal_to(expected_text))

    def test_hello_random(self):
        self.setUp()
        text = self.twitter_bot.get_hello_random()
        assert_that(text, not_none())
        print(text)

    def test_lucas_name(self):
        self.setUp()
        text = self.twitter_bot.get_lucas_name()
        assert_that(text, not_none())
        print(text)

    def test_screensaver(self):
        self.setUp()
        text = self.twitter_bot.get_screensaver()
        assert_that(text, not_none())
        print(text)

    def test_prince_song(self):
        self.setUp()
        text = self.twitter_bot.get_prince_song()
        assert_that(text, not_none())
        print(text)

    def test_quest_log(self):
        self.setUp()
        text = self.twitter_bot.get_quest_progress()
        assert_that(text, not_none())
        print(text)

    def test_congress_vote(self):
        self.setUp()
        text = self.twitter_bot.get_congress_vote()
        assert_that(text, not_none())
        print(text)

    def test_tweepy_api(self):
        self.setUp()
        text = self.twitter_bot.tweet('test')
        self.api.update_status.assert_called_once_with('test')
        assert_that(text, equal_to('test'))
