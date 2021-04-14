# Plugin Fake News Detector

A project made in the context of Coding Weeks, in its second phase.

## Membres

* Oussama JANAHEDDINE
* Fayssal DEFAA  
* Mohammed El Hamidi
* Yahya JANBOUBI

## Besoin
Vu l'abondance des flux des infos sur Twitter et l'impact négatif de la propagation des Fake News sur les decisions des internautes (Influence sur les éléctions par exemple) mais aussi sur la réputation des personnes concernées, il s'avère nécessaire de mettre en place un dispositif capable de détecter si un tweet comporte des Fake News.

## Solution 
Création d'une extension Chrome qui émmet un score de crédibilité et permet ainsi de filtrer les tweets susceptiles de contenir des Fake News.

## MVP 
Etablir un algorithme de détection de Fake News.

## To Get Started
1. Allez vers [***frequency.py***](/api/detector/frequency.py).
2. Renseignez le chemein vers le dossier api.   
3. Sauvegardez le changement.
4. Installez `twint` par la commande `python setup.py install` lancer depuis le dossier [**twint**](/api/twint).
5. Installez l'extension depuis les options developpeur dans Chrome.
6. Lancer l'api depuis le fichier [***api.py***](/api/api.py).
7. Allez au site [Twitter](http://twitter.com)
8. Cliquer sur l'extension et choisir le tweet à evaluer.


## Sprint

### Sprint 0: 
* Séance de créativité.
* Distribution des tâches.

### Sprint 1: Mise en place du cadre de travail sous [Twint](https://github.com/twintproject/twint)

#### Fonctionalité 1:
Prise en main de [Twint](https://github.com/twintproject/twint).

#### Fonctionalité 2:
Migrer les fonctions établies durant la semaine 1 de la plate-forme Tweepy vers Twint.

#### Fonctionalité 3:
Prétraitement des tweets reçus en les transformant en Pandas DataFrame.

### Sprint 2: 

#### Fonctionalité 1: Detection linguistique des indicateurs de Fake News
Détecter, à partir de l'activité autour du tweet, la présence de mots ou phrases indiquants le caractère faux du tweet et présentation du résultat sous forme d'un score de crédibilité.

#### Fonctionalité 2: Arborescence des utilisateurs
Estimer la crédibilité du tweet à partir du status de son auteur (Verifié ou non) et des acteurs y figurant dans l'activité autour du tweet.

#### Fonctionalité 3: Analyse de sentiments
Prédire le caratère légitime du tweet à partir de la concordance de la réaction du public avec le contenu du tweet et sa subjectivité.  

#### Fonctionalité 4: Analyse fréquentielle 
Analyser la frequence d'apparition des mots clés dans un tweet pour y accorder un index de crédibilité en fonction de la base de données des tweets.

### Sprint 3:

#### Fonctionalité 1:
Combiner les différents criteres de détection de Fake News afin de mettre un seul score basé sur une combinaison biaisée des autres.

#### Fonctionalité 2:
Tester l'algorithme et mesurer sa fiabilité.

### Sprint 4:

#### Fonctionalité 1:
Implémentation de l'extension grace à la  bibliothèque RapydScript qui transforme notre code Python en Javascript.

#### Fonctionalité 2:
Création d'une page d'acceuil pour notre extension.

#### Fonctionalité 3:
Ajout des nouvelles fonctionalités à notre extension et optimisation du fonctionnement.
