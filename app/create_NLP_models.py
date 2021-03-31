# This creates NLP models using TfidfVectorizer for Wikipedia and Reddit Datasets
import spacy
import numpy as np
import dill
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from spacy.lang.en.stop_words import STOP_WORDS
from sklearn.linear_model import LogisticRegression
from sklearn import base
nlp = spacy.load("en_core_web_sm")


def tokenize_lemma(text):
    return [w.lemma_.lower() for w in nlp(text)]

def train_label(d):
    """
    Creates training and labels for model based on dictionary wikipedia structure
    """
    train = []
    for ele in d.values():
        train.extend(ele)    
    labels = []
    labels+= [[k]*len(d[k]) for k in d.keys()]
    labels = [item for sublist in labels for item in sublist]    
    return train, labels



# Load Wikipedia and Reddit data:
reddit_spirits = dill.load(open('model_data/reddit_spirits.pkd', 'rb'))
spirit_wiki = dill.load(open('model_data/spirit_wiki.pkd', 'rb'))
liqueur_wiki = dill.load(open('model_data/liqueur_wiki.pkd', 'rb'))
juice_wiki = dill.load(open('model_data/juice_wiki.pkd', 'rb'))
syrup_wiki = dill.load(open('model_data/syrup_wiki.pkd', 'rb'))
other_wiki = dill.load(open('model_data/other_wiki.pkd', 'rb'))



# Get training set and labels for models:
spirit_train,spirit_labels = train_label(spirit_wiki)
liqueur_train,liqueur_labels = train_label(liqueur_wiki)
juice_train,juice_labels = train_label(juice_wiki)
syrup_train,syrup_labels = train_label(syrup_wiki)
other_train,other_labels = train_label(other_wiki)




###############################################
# MAKE MODEL PREDICTIONS AND SAVE:
####################################################
stop_words_lemma = set(tokenize_lemma(' '.join(STOP_WORDS)))
tfid = TfidfVectorizer(ngram_range=(1,2),stop_words=stop_words_lemma,tokenizer=tokenize_lemma) # tfid vectorizer
# JUICE PREDICTION:
juice_model = Pipeline([('features', tfid),
                 ('classifier', LogisticRegression(class_weight='balanced'))])
juice_model.fit(juice_train,juice_labels)
dill.dump(juice_model, open('model_data/juice_model.pkd', 'wb'))
print('Juice model saved')

# SPIRIT PREDICTION:
spirit_model = Pipeline([('features', tfid),
                 ('classifier', LogisticRegression(class_weight='balanced'))])
spirit_model.fit(spirit_train,spirit_labels)
dill.dump(spirit_model, open('model_data/spirit_model.pkd', 'wb'))
print('Spirit model saved')

# LIQUEUR PREDICTION:
liqueur_model = Pipeline([('features', tfid),
                 ('classifier', LogisticRegression(class_weight='balanced'))])
liqueur_model.fit(liqueur_train,liqueur_labels)
dill.dump(liqueur_model, open('model_data/liqueur_model.pkd', 'wb'))

# SYRUP PREDICTION:
syrup_model = Pipeline([('features', tfid),
                 ('classifier', LogisticRegression(class_weight='balanced'))])
syrup_model.fit(syrup_train,syrup_labels)
dill.dump(syrup_model, open('model_data/syrup_model.pkd', 'wb'))

# OTHER PREDICTION:
other_model = Pipeline([('features', tfid),
                 ('classifier', LogisticRegression(class_weight='balanced'))])
other_model.fit(other_train,other_labels)
dill.dump(other_model, open('model_data/other_model.pkd', 'wb'))

# REDDIT PREDICTION:
reddit_train,reddit_labels = train_label(reddit_spirits)
reddit_model = Pipeline([('features', tfid),
                 ('classifier', LogisticRegression(class_weight='balanced'))])
reddit_model.fit(reddit_train,reddit_labels)
dill.dump(reddit_model, open('model_data/reddit_model.pkd', 'wb'))