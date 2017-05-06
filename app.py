import logging, os, time, tweepy
import config

# CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
# CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
# ACCESS_KEY = os.environ.get('ACCESS_KEY')
# ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_KEY = config.ACCESS_KEY
ACCESS_SECRET = config.ACCESS_SECRET


class TwitterBot():
    def __init__(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def tweet(self, msg=None):
        self.api.update_status(msg or 'Hello World')


if __name__ == "__main__":
    twitterbot = TwitterBot()
    logger = logging.getLogger('__main__')
    for _ in range(2):
        twitterbot.tweet('Tweetin a phrase ' + str(_))
        logger.debug('Tweeted ur phrase')
        time.sleep(10)
