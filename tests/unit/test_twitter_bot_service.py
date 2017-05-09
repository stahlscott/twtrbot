from hamcrest import *
from mock import MagicMock

from app.services.random_phrase_service import RandomPhraseService
from app.services.twitter_bot_service import TwitterBotService


class TestTwitterBot():
    def setUp(self):
        self.api = MagicMock()
        self.db = MagicMock()
        self.dao = RandomPhraseService(db=self.db)
        self.twitter_bot = TwitterBotService(api=self.api, db=self.db)

    # TODO Rewrite working tests
    #
    # def test_lucas_name(self):
    #     self.setUp()
    #     text = self.twitter_bot.get_lucas_name()
    #     assert_that(text, not_none())
    #
    # def test_screensaver(self):
    #     self.setUp()
    #     text = self.twitter_bot.get_screensaver()
    #     assert_that(text, not_none())
    #
    # def test_prince_song(self):
    #     self.setUp()
    #     text = self.twitter_bot.get_prince_song()
    #     assert_that(text, not_none())
    #
    # def test_quest_log(self):
    #     self.setUp()
    #     text = self.twitter_bot.get_quest_progress()
    #     assert_that(text, not_none())
    #
    # def test_congress_vote(self):
    #     self.setUp()
    #     text = self.twitter_bot.get_congress_vote()
    #     assert_that(text, not_none())
    #
    # def test_tweepy_api(self):
    #     self.setUp()
    #     text = self.twitter_bot.tweet('test')
    #     self.api.update_status.assert_called_once_with('test')
    #     assert_that(text, equal_to('test'))
