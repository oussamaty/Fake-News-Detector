from detector.user import *
from pytest import *

def test_percentage_tweet_keywords():
    assert 0 <= percentage_tweet_keywords(get_tweets('Biden won the election',1,True,False,False).loc[0],['biden','won']) <= 1

def test_top_10_similar():
    assert 0 <= len(top_10_similar(get_tweets('Biden won the election',1,True,False,False).loc[0])) <= 10

def test_score_user():
    assert 0 <= score_user(get_tweets('Biden won the election',1,True,False,False).loc[0]) <= 1