from random import choice, randint
from app.generator_data import *


class RandomGenerator():
    def hello_random(self):
        return [choice(GREETINGS), choice(NOUNS)]

    def lucas_name(self):
        return [choice(LUCAS_FIRST_NAMES), choice(LUCAS_LAST_NAMES)]

    def screensaver(self):
        return [choice(SCREENSAVER_ADJECTIVE), choice(SCREENSAVER_NOUN)]

    def prince_song(self):
        rand_int = randint(1, 8)
        prefix = choice(PRINCE_PREFIXES) if rand_int in [1] else ''
        suffix = choice(PRINCE_SUFFIXES) if rand_int in [2, 3, 4] else ''
        adjective = choice(PRINCE_ADJECTIVES)
        noun = choice(PRINCE_NOUNS)
        return [prefix, adjective, noun, suffix]

    def quest_log(self):
        max_num = 10
        total_num = randint(2, max_num) * 2
        in_progress_num = randint(1, total_num)
        quest_progress = str(in_progress_num) + '/' + str(total_num)

        return [quest_progress, choice(QUEST_LOG_DESCRIPTOR), choice(QUEST_LOG_NOUNS), choice(QUEST_LOG_ACTION)]

    def congress_vote(self):
        return [choice(CONGRESS_TITLE), choice(CONGRESS_LAST_NAME), choice(CONGRESS_PARTY), choice(CONGRESS_STATE),
                choice(CONGRESS_VOTE), str(randint(1, 999)), choice(CONGRESS_VERB), choice(CONGRESS_NOUN)]
