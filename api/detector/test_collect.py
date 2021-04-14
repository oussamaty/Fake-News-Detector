from detector.collect import *
from pytest import *


def test_get_tweets():
    tweets = get_tweets('Donald Trump')
    assert 'id' in tweets.columns

def test_get_candidate_tweets():
    tweets = get_candidate_tweets('realdonaldtrump')
    assert 'id' in tweets.columns and tweets['username'].loc[0] == 'realDonaldTrump'

def test_get_user_info():
    user_info = get_user_info('realdonaldtrump')
    assert 'verified' in user_info.columns and len(user_info) > 0

def test_get_replies_to_tweet():
    tweet = get_candidate_tweets("realdonaldtrump",1,True,False,False).loc[0]
    replies = get_replies_to_tweet(tweet)
    assert hasattr(replies[0],'id')
