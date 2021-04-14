import pandas as pd 
import numpy as np 
import string
import nltk 
import pickle
from textblob import TextBlob
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import feature_extraction, linear_model, model_selection, preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# nltk.download('stopwords')

path = ' rentrez le path vers le dossier api ici '

def traitement_tweet(text):
    '''
    entrée : texte
    sortie : texte en miniscule sans stop words ni ponctuation où le smots sont rendus à leur racine
    '''
    stop = stopwords.words('english')
    return ' '.join([word.lemmatize().lower() for word in TextBlob(text).words if word not in stop and word not in string.punctuation])

def traitement_data(data):
    '''
    entrée : dataframe pandas
    sortie : dataframe pandas avec des textes traités

    '''
    result = pd.DataFrame(columns=['text','truth'])
    for i in data.index:
        treated_tweet = traitement_tweet(data['text'][i])
        result.loc[i] = [treated_tweet,data['truth'][i]]
    return result
    
def save_data(data,filename):
    '''
    entrée : Dataframe pandas
    sortie : sauvegrade la data dans un fichier 
    '''
    data.to_csv(path+ "/dataset/" + filename + ".csv")

def save_model(datapath,filename):
    '''
    entrée : chaine de caractères représentant l'emplacement choisi pour le fichier
    sortie : sauvegarde l'état du réseau de neuronnes (weights)

    '''
    data = pd.read_csv(datapath)
    X_train,X_test,y_train,y_test= train_test_split(data['text'].apply(lambda x: np.str_(x)), data['truth'], test_size=0.2, random_state=42)
    pipe = Pipeline([('vect', CountVectorizer()),
                 ('tfidf', TfidfTransformer()),
                 ('model', LogisticRegression())])
    # Fitting the model
    model = pipe.fit(X_train, y_train)
    # save the model to disks
    pickle.dump(model, open(path + '/model/' + filename, 'wb'))

def load_model(filepath):
    '''
    entrée : chaine de caractères représentant l'emplacement choisi pour le fichier
    sortie : extrait l'état du réseau de neuronnes (weights)

    '''
    return pickle.load(open(filepath, 'rb'))

def score_frequence(tweet):
    '''
    entrée : tweet
    sortie : score de crédibilité généré par une approche statistique de machine learning

    '''
    return load_model(path + '/model/finalized_model.sav').predict_proba([tweet['tweet']])[0,0]

"""
def word_cloud(data):
    all_words = ' '.join([text for text in data.text])

    wordcloud = WordCloud(width= 800, height= 500, max_font_size = 110, collocations = False).generate(all_words)

    plt.figure(figsize=(10,7))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

words = data[data['truth'] == 'no']

word_cloud(words)
"""