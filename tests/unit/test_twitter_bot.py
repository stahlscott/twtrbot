from hamcrest import *
from mock import MagicMock

from app.twitter_bot import TwitterBot


class TestTwitterBot():
    def setUp(self):
        self.api = MagicMock()
        self.twitter_bot = TwitterBot(api=self.api)

    def test_get_text_none(self):
        self.setUp()
        text = self.twitter_bot._get_basic_text(text=None)
        expected_text = 'Hello World!'
        assert_that(text, equal_to(expected_text))

    def test_hello_random(self):
        self.setUp()
        text = self.twitter_bot._get_hello_random()
        expected_text = 'Hello '
        assert_that(text, contains_string(expected_text))
