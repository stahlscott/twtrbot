from app.random_generator import RandomGenerator


class TwitterBot():
    def __init__(self, api):
        self._api = api
        self._generator = RandomGenerator()

    def _tweet(self, text):
        # TODO Catch exceptions
        self._api.update_status(text)
        return text

    def tweet_basic(self, text=None):
        text = self._get_basic_text(text=text)
        return self._tweet(text)

    def _get_basic_text(self, text):
        return text or 'Hello World!'

    def tweet_random(self):
        text = self._get_hello_random()
        return self._tweet(text=text)

    def _get_hello_random(self):
        return 'Hello ' + self._generator.noun() + '!'

    def tweet_lucas_name(self):
        text = self._get_lucas_name()
        return self._tweet(text=text)

    def _get_lucas_name(self):
        name = self._generator.lucas_name()
        return name[0] + ' ' + name[1]
