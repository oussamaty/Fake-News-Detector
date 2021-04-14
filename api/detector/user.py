from detector.collect import *
from textblob import TextBlob ,Word
import numpy as np
import pandas as pd

query_factor = 5
user_factor = 0.3

def percentage_tweet_keywords(tweet,keywords):
    '''
    entrée : tweet, keywords(liste de chaines de caractères)
    sortie : pourcentage des keywords présents dans le tweet
    #va servir de critère de similarité
    '''
    tweet_full_text_words=str(tweet).split()
    s=0
    for word_1 in tweet_full_text_words:
        for word_2 in keywords:
            if Word(word_1).lemmatize()==Word(word_2).lemmatize():
                s+=1
    return s/len(tweet_full_text_words)

def get_top_10(tweets):
    '''
    entrée : liste de listes (listes internes comprenant 2 éléments)
    sortie : liste de listes après sélections des 10 lignes ordonnées par la 2ème colonne

    '''
    result = tweets.sort_values(by=['pourcentage'], ascending=False).reset_index()
    return result.head(10)


def top_10_similar(tweet_0):
    '''
    entrée : tweet
    sortie : les 10 tweets les plus similaire selon notre critère

    '''
    tweet_keywords = tweet_0["tweet"].split()
    potential_similar_tweets = pd.DataFrame()
    for i in range(len(tweet_keywords)//query_factor):
        tweet = ' '.join(tweet_keywords[i*query_factor:(i+1)*query_factor])
        tweets = get_tweets(tweet,True,10)
        potential_similar_tweets = pd.DataFrame([],columns=['tweet'])
        percentage = pd.DataFrame([],columns=['pourcentage'])
        try:
            potential_similar_tweets = potential_similar_tweets.append(pd.DataFrame(tweets['tweet'],columns=['tweet'])).reset_index(drop = True)
            p = pd.DataFrame([percentage_tweet_keywords(t,tweet_keywords) for t in tweets['tweet']],columns=['pourcentage'])
            percentage = percentage.append(p).reset_index(drop=True)
        except KeyError:
            pass   
    potential_similar_tweets['pourcentage'] = percentage
    percentage_tweet_keywords(potential_similar_tweets['tweet'],tweet_keywords)
    return get_top_10(potential_similar_tweets)

def score_user(tweet):
    '''
    entrée : tweet
    sortie : score basé sur les infos des utilisateurs en relation avec ce tweet

    '''
    n = 0
    s = 0
    if hasattr(tweet,'verified'):
        if tweet['verified']:
            n = 1
    top_10 = top_10_similar(tweet)
    if not top_10_similar(tweet).empty :
        s = np.sum(top_10['pourcentage'])/len(top_10)
    return (user_factor*n + s)/(user_factor + 1)


