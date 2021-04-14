from detector.frequence import *
from pytest import*
import pandas as pd

def test_traitement_tweet():
    assert traitement_tweet('Hello, World!? ')=='hello world'


def test_traitement_data():

    assert traitement_data(pd.DataFrame([['Hello, World!','yes']] , columns=['text','truth'])).equals(pd.DataFrame([['hello world','yes']], columns=['text','truth']))

def test_save_data():
    data = pd.DataFrame([['hello world','yes']], columns=['text','truth'])
    save_data(data,'test')
    assert 'text' in pd.read_csv(path +'dataset/test.csv').columns

def test_save_model():
    save_model(path+ "dataset/db.csv",'test_model')
    model = pickle.load(open(path + 'model/test_model.sav', 'rb'))
    assert isinstance(model,Pipeline) 

def test_load_model():
    model = load_model(path + 'model/test_model.sav')
    assert isinstance(model,Pipeline) 

def test_score_frequence():
    assert 0<=score_frequence({'tweet':'trump won the 2020 election'})<=1
