from hamcrest import *

from app.random_generator import RandomGenerator, NOUNS


class TestRandomGenerator():
    def setUp(self):
        self.generator = RandomGenerator()

    def test_get_noun(self):
        self.setUp()
        noun = self.generator.noun()
        assert_that(noun, is_in(NOUNS))

    def test_get_lucas_name(self):
        self.setUp()
        lucas_name = self.generator.lucas_name()
        # print(lucas_name[0] + ' ' + lucas_name[1])
        assert_that(lucas_name, has_length(2))
