from app.random_generator import RandomGenerator


class TwitterBot():
    def __init__(self, api):
        self._api = api
        self._generator = RandomGenerator()

    def _tweet(self, text):
        # TODO Catch exceptions
        self._api.update_status(text)
        return text

    def _get_basic_text(self, text):
        return text or 'Hello World!'

    def tweet_basic(self, text=None):
        text = self._get_basic_text(text=text)
        return self._tweet(text)

    def _get_hello_random(self):
        hello_random = self._generator.hello_random()
        return ' '.join(hello_random) + '!'

    def tweet_random(self):
        hello_random = self._get_hello_random()
        return self._tweet(text=hello_random)

    def _get_lucas_name(self):
        name = self._generator.lucas_name()
        return ' '.join(name)

    def tweet_lucas_name(self):
        lucas_name = self._get_lucas_name()
        return self._tweet(text=lucas_name)

    def _get_screensaver(self):
        screensaver = self._generator.screensaver()
        return ' '.join(screensaver)

    def tweet_screensaver(self):
        screensaver = self._get_screensaver()
        return self._tweet(screensaver)

    def _get_prince_song(self):
        prince_song = self._generator.prince_song()
        return (' '.join(prince_song)).strip()

    def tweet_prince_song(self):
        prince_song = self._get_prince_song()
        return self._tweet(prince_song)

    def _get_quest_progress(self):
        quest = self._generator.quest_log()
        return ' '.join(quest)

    def tweet_quest_progress(self):
        quest_progress = self._get_quest_progress()
        return self._tweet(quest_progress)

    def _get_congress_vote(self):
        vote = self._generator.congress_vote()
        formatted_vote = vote[0] + ' ' + vote[1] + ' (' + vote[2] + '-' + vote[3] + ') votes ' + vote[4] + ' on HR ' + \
                         vote[5] + ' to ' + vote[6] + ' ' + vote[7]
        return formatted_vote

    def tweet_congress_vote(self):
        vote = self._get_congress_vote()
        return self._tweet(vote)
