from detector.sentiment import *
from detector.collect import *
from pytest import *


def test_tweet_subjectivity():
    tweet = get_candidate_tweets('realdonaldtrump',1,True,False,False).loc[0]
    subjectivity = tweet_subjectivity(tweet)
    assert 0 <=  subjectivity <= 1


def test_sentiment_analysis():
    tweet = get_candidate_tweets('realdonaldtrump',1,True,False,False).loc[0]
    index = sentiment_analysis(tweet)
    assert 0 <= index <= 1


def test_score_sentiment():
    tweet = get_candidate_tweets('realdonaldtrump',1,True,False,False).loc[0]
    score = score_sentiment(tweet)
    assert 0 <= score <= 1