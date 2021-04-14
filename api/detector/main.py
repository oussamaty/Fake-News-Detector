from detector.collect import *
from detector.fake import *
from detector.sentiment import *
from detector.user import *
from detector.frequence import *
import pandas as pd

def treat_tweet(tweet):
        tweet_id = tweet['id']
        conversation_id = tweet['id']
        date = tweet['date']
        tweet_text = tweet['tweet']
        username = tweet['username']
        if hasattr(tweet,'like_count'):
            nlikes = tweet['like_count']
        else:
            nlikes = 0
        if hasattr(tweet,'retweet_count'):
            nretweets = tweet['retweet_count']
        else:
            nretweets = 0
        if hasattr(tweet,'replies_count'):
            nreplies = tweet['replies_count']
        else:
            nreplies = 0
        if hasattr(tweet,'verified'):    
            verified = tweet['verified']
        else:
            verified = None
        if hasattr(tweet,'reply_to'):
            reply_to = tweet['reply_to']
        else:
            reply_to = []
        if hasattr(tweet,'referenced_tweets'):
            referenced_tweets = tweet['referenced_tweets']
        else:
            referenced_tweets = []
        if hasattr(tweet,'geo'):
            geo = tweet['geo']
        else:
            geo = []
        values = [[tweet_id,conversation_id,date,tweet_text,username,nlikes,nretweets,nreplies,verified,reply_to,referenced_tweets,geo]]
        columns = ['id','conversation_id','date', 'tweet','username','nlikes','nretweets','nreplies','verified','reply_to','referenced_tweets','geo']
        data = pd.DataFrame(values,columns=columns)
        return data

def credibility_score(tweet,weights):
    w_fake = weights[0]
    w_sentiment = weights[1]
    w_frequence = weights[2]
    w_user = weights[3]
    score = (w_fake*score_fake(tweet) + w_sentiment*score_sentiment(tweet) + w_user*score_user(tweet) + w_frequence*score_frequence(tweet))
    return score

def get_score(tweet,weights = [0.3,0.3,0.3,0.1]):
    status = treat_tweet(tweet).loc[0]
    return 1 - credibility_score(status,weights)