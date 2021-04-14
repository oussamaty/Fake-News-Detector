from detector.collect import *
from textblob import TextBlob

facteur_sentiment = 4

def tweet_subjectivity(tweet):
    return TextBlob(tweet['tweet']).sentiment.subjectivity

def sentiment_analysis(tweet):
    replies = get_replies_to_tweet(tweet)
    sentiments = []
    tweet_sentiment = TextBlob(tweet['tweet']).sentiment.polarity
    index = 0
    normaliseur = 1
    for reply in replies:
        coeff = reply['nlikes'] + reply['nretweets']
        index += TextBlob(reply['tweet']).sentiment.polarity*coeff*tweet_sentiment
        normaliseur += coeff
    index = index/normaliseur
    return  (index + 1)/2

def score_sentiment(tweet):
    return 1 - (tweet_subjectivity(tweet) + facteur_sentiment*sentiment_analysis(tweet))/(facteur_sentiment + 1) 
