import logging

import tweepy

from app.twitter_bot import TwitterBot


def tweepy_api(config):
    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
    return tweepy.API(auth)


def send_tweet(twitter_bot):
    return twitter_bot.tweet_basic()
    # TODO catch exceptions ?
    # wait_time = 60 * 60
    # time.sleep(wait_time)


def run(config):
    api = tweepy_api(config)
    twitter_bot = TwitterBot(api=api)
    logger = logging.getLogger('app.run')

    for _ in range(1):  # TODO Make it run forever?
        text = send_tweet(twitter_bot)
        logger.debug('Tweeted ur phrase: ' + text)
