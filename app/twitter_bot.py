from app.random_generator import RandomGenerator


class TwitterBot():
    def __init__(self, api):
        self._api = api
        self._generator = RandomGenerator()

    def tweet(self, text):
        # TODO Catch exceptions
        self._api.update_status(text)
        return text

    def get_basic_text(self, text):
        return text or 'Hello World!'

    def tweet_basic(self, text=None):
        text = self.get_basic_text(text=text)
        return self.tweet(text)

    def get_hello_random(self):
        hello_random = self._generator.hello_random()
        return ' '.join(hello_random) + '!'.strip()

    def tweet_random(self):
        hello_random = self.get_hello_random()
        return self.tweet(text=hello_random)

    def get_lucas_name(self):
        name = self._generator.lucas_name()
        return ' '.join(name).strip()

    def tweet_lucas_name(self):
        lucas_name = self.get_lucas_name()
        return self.tweet(text=lucas_name)

    def get_screensaver(self):
        screensaver = self._generator.screensaver()
        return ' '.join(screensaver).strip()

    def tweet_screensaver(self):
        screensaver = self.get_screensaver()
        return self.tweet(screensaver)

    def get_prince_song(self):
        prince_song = self._generator.prince_song()
        return ' '.join(prince_song).strip()

    def tweet_prince_song(self):
        prince_song = self.get_prince_song()
        return self.tweet(prince_song)

    def get_quest_progress(self):
        quest = self._generator.quest_log()
        return ' '.join(quest).strip()

    def tweet_quest_progress(self):
        quest_progress = self.get_quest_progress()
        return self.tweet(quest_progress)

    def get_congress_vote(self):
        vote = self._generator.congress_vote()
        formatted_vote = '{0} {1} ({2}-{3}) votes {4} on HR {5} to {6} {7}'.format(*vote)
        return formatted_vote.strip()

    def tweet_congress_vote(self):
        vote = self.get_congress_vote()
        return self.tweet(vote)
