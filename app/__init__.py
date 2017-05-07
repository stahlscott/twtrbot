from collections import namedtuple
from flask import Flask, render_template
import logging
import os
import tweepy

from app.twitter_bot import TwitterBot

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY')

TweetTuple = namedtuple('TweetTuple', ['text', 'img', 'handle'])


def tweepy_api():
    auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
    auth.set_access_token(os.environ.get('ACCESS_KEY'), os.environ.get('ACCESS_SECRET'))
    return tweepy.API(auth)


def send_tweet(twitter_bot):
    return twitter_bot.tweet_prince_song()
    # TODO catch exceptions ?
    # wait_time = 60 * 60
    # time.sleep(wait_time)


def run():
    api = tweepy_api()
    twitter_bot = TwitterBot(api=api)
    logger = logging.getLogger('app.run')

    for _ in range(1):  # TODO Make it run forever?
        text = send_tweet(twitter_bot)
        logger.debug('Tweeted ur phrase: ' + text)


@app.route('/')
def twtrbot():
    twitter_bot = TwitterBot(api=None)
    lucas_name = TweetTuple(text=twitter_bot.get_lucas_name(), handle='@GeorgeLucasAssNames',
                            img='/static/img/lucas.png')
    prince_song = TweetTuple(text=twitter_bot.get_prince_song(), handle='@PrinceVault',
                             img='/static/img/prince.png')
    screensaver = TweetTuple(text=twitter_bot.get_screensaver(), handle='@NewScreensavers',
                             img='/static/img/screensaver.png')
    quest_log = TweetTuple(text=twitter_bot.get_quest_progress(), handle='@QuestProgress',
                           img='/static/img/quest.png')
    congress_vote = TweetTuple(text=twitter_bot.get_congress_vote(), handle='@CongressVotes',
                               img='/static/img/vote.png')

    tweets = [lucas_name, prince_song, screensaver, quest_log, congress_vote]
    return render_template('twtrbot.html', tweets=tweets)
