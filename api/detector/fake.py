from detector.collect import *
import numpy as np
import pandas as pd
from textblob import TextBlob, Word
import re
import collections
import itertools

most_commun = 20
#choix du nombre de mots les plus fréquents à garder
query_split_factor = 4
#on divise la requête en sous requête modulo 4
fake_indicators_list = ["fake", "hoax", "rumor", "lie",'misinformation','wrong','fakenews','liar','fraud', 'deny', 'denies', 'not true', 'rumeur', 'faux']
#liste des indicateurs linguistiques


def deEmojify(text):
    '''
    entrée : texte
    sortie : texte après suppression des emojis
    
    '''
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

def tweets_words(data,query,repetitive = False):
    '''

    entrées : database panda, keywords
    sortie : liste de listes (une liste interne correspondant à un tweet) des mots séparés du texte des tweets
             

    '''
    stop_words = set( " - — _ a m about above after again against n't all am an and any are ’ “ ” aren http : / \\ https 's 're 've 't 'd 'll 'm ' ll \" u s ve t d re as at be because been before being below between both but by can 't cannot could couldn 't did didn 't do does doesn 't doing don 't down during each few for from further had hadn has hasn have haven having he he 'd he 'll he 's her here here 's hers herself him himself his how how 's i i 'd i 'll i 'm i 've if in into is isn 't it it 's its itself let 's me more most mustn 't my myself no nor not of off on once only or other ought our ours ourselves out over own same shan 't she she 'd she 'll she 's should shouldn 't so some such than that that 's the their theirs them themselves then there there 's these they they'd they'll they're they've this those through to too under until up very was wasn't we we'd we'll we're we've were weren't what what's when when's where where's which while who who's whom why why's with won't would wouldn't you you'd you 'll you 're you 've your yours yourself yourselves".split(' ')) #set("kjsdjkrkjgr")
    total_tweets = []
    try:
        for i in range(len(data['id'])):
            l = []
            for w in TextBlob(deEmojify(data['tweet'].iloc[i].lower())).words:
                if not w.isnumeric() and not 't.co' in w and w not in stop_words:
                    l.append(Word(w).lemmatize())
            if repetitive:
                total_tweets.append(l)
            else :
                total_tweets.append(list(set(l)))
    except KeyError:
        pass
    return total_tweets


def frequency_words(data,query):
    '''
    entrées : Database pandas, keywords
    sortie : database panda des 20 mots les plus récurrents dans les tweets avec leur total d'apparition

    '''
    return pd.DataFrame(collections.Counter(list(itertools.chain(*tweets_words(data,query)))).most_common(most_commun),columns=['words', 'count'])


def score_fake(tweet):
    '''
    entrée : tweet
    sortie : score par la détection linguistique des mots

    '''
    query = tweets_words(pd.DataFrame().append(tweet),"",True)[0]
    queries = [" ".join(query[query_split_factor*i:query_split_factor*(i+1)]) for i in range(len(query)//query_split_factor)]
    words = pd.DataFrame()
    for q in queries:
        words = words.append(frequency_words(get_tweets(q,count=50), q)).reindex()
    counter = 0
    score = 0
    for i in words.index:
        if  words['words'].iloc[i] in fake_indicators_list:
            score += words['count'].iloc[i]/np.max(words['count'])
            counter += 1
    if counter == 0:
        return 0
    return 1 - score/counter















