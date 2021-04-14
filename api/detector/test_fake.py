from detector.fake import *
from pytest import *

def test_deEmojify():
    text = 'hello😁'
    assert deEmojify(text) == 'hello'

def test_tweets_words():
    words = tweets_words(get_candidate_tweets('realdonaldtrump',1,True,False,False),'trump')
    assert 'the' not in words[0]

def test_frequency_words():
    db = frequency_words(get_candidate_tweets('realdonaldtrump',1,True,False,False),'trump')
    assert 'words' in db.columns

def test_score_fake():
    tweet = get_candidate_tweets('realdonaldtrump',1,True,False,False).loc[0]
    score = score_fake(tweet) == 0
    assert 0 <= score <= 1

