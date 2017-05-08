from random import choice, randint
from app.generator_data import *


class RandomPhraseDAO():
    def hello_random(self):
        return [choice(GREETINGS), choice(NOUNS)]

    def lucas_name(self):
        return [choice(LUCAS_FIRST_NAMES), choice(LUCAS_LAST_NAMES)]

    def screensaver(self):
        # adverb = choice(SCREENSAVER_ADVERBS) if not randint(0, 2) else ''
        return [choice(SCREENSAVER_DESCRIPTORS), choice(SCREENSAVER_NOUNS)]

    def prince_song(self):
        rand_int = randint(1, 10)
        prefix_odds = [1, 2]
        suffix_odds = [2, 3, 4, 5]

        prefix = choice(PRINCE_PREFIXES) if rand_int in prefix_odds else ''
        suffix = choice(PRINCE_SUFFIXES) if rand_int in suffix_odds else ''
        adjective = choice(PRINCE_ADJECTIVES)
        noun = choice(PRINCE_NOUNS)

        return [prefix, adjective, noun, suffix]

    def quest_log(self):
        max_num = 10
        total_num = randint(2, max_num) * 2
        in_progress_num = randint(1, total_num)
        quest_progress = str(in_progress_num) + '/' + str(total_num)
        completed = ' (COMPLETED)' if total_num == in_progress_num else ''

        rand_int = randint(1, 10)
        prefix = choice(QUEST_LOG_NOUN_PREFIX) + ' ' if 4 <= rand_int <= 8 else ''

        if rand_int > 5:
            noun = prefix + choice(QUEST_LOG_NOUN)
            action = choice(QUEST_LOG_COLLECTED_PARTS) + ' Collected'
        else:
            noun = prefix + choice(QUEST_LOG_NOUN) + 's'  # pluralize
            action = choice(QUEST_LOG_ACTIONS)

        return [quest_progress, noun, action, completed]

    def congress_vote(self):
        return [choice(CONGRESS_TITLE), choice(CONGRESS_LAST_NAME), choice(CONGRESS_PARTY), choice(CONGRESS_STATE),
                choice(CONGRESS_VOTE), str(randint(1, 5999)), choice(CONGRESS_VERB), choice(CONGRESS_NOUN)]
