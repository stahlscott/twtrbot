from hamcrest import *

from app.daos.random_phrase_dao import RandomPhraseDAO, NOUNS


class TestRandomPhraseDAO():
    def setUp(self):
        self.generator = RandomPhraseDAO()

    def test_get_noun(self):
        self.setUp()
        hello_random = self.generator.hello_random()
        assert_that(hello_random, has_length(2))
        assert_that(hello_random[1], is_in(NOUNS))

    def test_get_lucas_name(self):
        self.setUp()
        lucas_name = self.generator.lucas_name()
        assert_that(lucas_name, has_length(2))

    def test_get_screensaver(self):
        self.setUp()
        screensaver = self.generator.screensaver()
        assert_that(screensaver, has_length(2))

    def test_get_prince_song(self):
        self.setUp()
        prince_song = self.generator.prince_song()
        assert_that(prince_song, not_none())

    def test_get_quest(self):
        self.setUp()
        quest = self.generator.quest_log()
        assert_that(quest, has_length(4))

    def test_get_vote(self):
        self.setUp()
        vote = self.generator.congress_vote()
        assert_that(vote, has_length(8))
