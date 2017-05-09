import os
from collections import namedtuple

import tweepy
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from app.services.twitter_bot_service import TwitterBotService

# flask setup
app = Flask(__name__, static_folder='../static')
app.secret_key = os.environ.get('SECRET_KEY')

# sqlalchemy setup
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# these import db so need to be imported after its definition
from app.daos.component_dao import ComponentDAO
from app.daos.component_type_dao import ComponentTypeDAO
from app.daos.phrase_dao import PhraseDAO

TweetTuple = namedtuple('TweetTuple', ['text', 'img_path', 'handle'])


def tweepy_api():
    auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
    auth.set_access_token(os.environ.get('ACCESS_KEY'), os.environ.get('ACCESS_SECRET'))
    return tweepy.API(auth)


def run():
    api = tweepy_api()
    twitter_bot_service = TwitterBotService(component_type_dao=ComponentTypeDAO(db=db),
                                            component_dao=ComponentDAO(db=db),
                                            api=api)

    text = twitter_bot_service.tweet_prince_song()
    app.logger.debug('Tweeted phrase: ' + text)


@app.route('/')
def twtrbot():
    twitter_bot_service = TwitterBotService(component_type_dao=ComponentTypeDAO(db=db),
                                            component_dao=ComponentDAO(db=db))
    phrase_dao = PhraseDAO(db=db)
    lucas_name = TweetTuple(text=twitter_bot_service.get_lucas_name(),
                            handle='@' + phrase_dao.get_phrase_by_name('LucasName').display_name,
                            img_path='img/lucas.png')
    prince_song = TweetTuple(text=twitter_bot_service.get_prince_song(),
                             handle='@' + phrase_dao.get_phrase_by_name('PrinceSong').display_name,
                             img_path='img/prince.png')
    screensaver = TweetTuple(text=twitter_bot_service.get_screensaver(),
                             handle='@' + phrase_dao.get_phrase_by_name('Screensaver').display_name,
                             img_path='img/screensaver.png')
    quest_log = TweetTuple(text=twitter_bot_service.get_quest_progress(),
                           handle='@' + phrase_dao.get_phrase_by_name('QuestLog').display_name,
                           img_path='img/quest.png')
    congress_vote = TweetTuple(text=twitter_bot_service.get_congress_vote(),
                               handle='@' + phrase_dao.get_phrase_by_name('CongressVote').display_name,
                               img_path='img/vote.png')

    tweets = [lucas_name, prince_song, screensaver, quest_log, congress_vote]
    return render_template('twtrbot.html', tweets=tweets)
