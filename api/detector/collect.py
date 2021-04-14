import twint
import pandas as pd
import datetime

def get_tweets(query,verified = False, count = 100, popular = False,retweets = True, replies = True):
    tweets = []
    try :
        c = twint.Config()
        c.Search = query
        c.Limit = count
        c.Retweets = retweets
        c.Replies = replies
        c.Popular_tweets = popular
        c.Pandas = True
        c.Store_json = True
        c.Verified = verified
        c.Hide_output = True
        twint.run.Search(c)
        tweets = twint.storage.panda.Tweets_df
    except Exception as e:
        raise e
    return tweets


def get_candidate_tweets(name_candidate,count = 100,popular = False,retweets = True, replies = True):
    tweets = []
    try :
        c = twint.Config()
        c.Username = name_candidate
        c.Limit = count
        c.Retweets = retweets
        c.Replies = replies
        c.Popular_tweets = popular
        c.Pandas = True
        c.Store_json = True
        c.Hide_output = True
        twint.run.Search(c)
        tweets =   twint.storage.panda.Tweets_df
    except Exception as e:
        raise e
    return tweets

def get_user_info(name_candidate):
    tweets = []
    try :
        c = twint.Config()
        c.Username = name_candidate
        c.Pandas = True
        c.Store_json = True
        c.Hide_output = True
        twint.run.Lookup(c)
        tweets =   twint.storage.panda.User_df
    except Exception as e:
        raise e
    return tweets


def get_replies_to_tweet(status):
    replies = []
    try :
        tweets = []
        c = twint.Config()
        c.Limit = 100
        c.Search = "@" + status['username']
        c.Since = status['date']
        until = datetime.datetime.strptime(status['date'],"%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=7)
        if until < datetime.datetime.now():
            c.Until = until.strftime("%Y-%m-%d %H:%M:%S")
        c.Retweets = False
        c.Replies = replies
        c.Popular_tweets = True
        c.Pandas = True
        c.Store_json = True
        c.Hide_output = True
        twint.run.Search(c)
        tweets =   twint.storage.panda.Tweets_df
        for i in tweets.index:
            if tweets['conversation_id'].loc[i] == status['conversation_id']:
                replies.append(tweets.loc[i])
    except Exception as e:
        raise e
    return replies


