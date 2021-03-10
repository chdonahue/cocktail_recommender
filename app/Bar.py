import pickle
import dill
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize
import numpy as np
from scipy import spatial
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
from collections import Counter
from bartender_mappings import ingredient_dict


# Unpickle data and load important info:
with open("cocktails.pickle", "rb") as file:
    cocktails = pickle.load(file)  
embedding_dict = dill.load(open('embedding_dict.pkd', 'rb'))
categories = list(ingredient_dict.keys())
categories.remove('garnish') # remove garnish
categories.remove('fruits') # remove fruits
lancaster=LancasterStemmer()



class Cocktails:
    def __init__(self):
        self.all_cocktails = cocktails # Full cocktail directory by title
        self.my_cocktails = {} # cocktails I can currently make in my bar
        self.my_ingredients = ['garnish','fruits'] # list of my ingredients (must come from ingredient_dict.keys())
        
    def update_menu(self):
        for key in self.all_cocktails:
            if all(ele in self.my_ingredients for ele in self.all_cocktails[key]['category']) and key not in self.my_cocktails.keys():
                self.my_cocktails[key] = self.all_cocktails[key]  
        
    def add_ingredients(self,ingredients): # List of ingredients to add (must come from ingredient_dict.keys())
        new_ingredients = list(set(ingredients)&set(ingredient_dict.keys())|set(self.my_ingredients))
        self.my_ingredients = new_ingredients
        self.update_menu()
        
    def __str__(self): # Prints list of cocktails
        return f'\n'.join(list(self.my_cocktails.keys()))






class Word2Cocktail:
    def __init__(self):
        self.query = [] 
        self.ingr_list = [] # ingredient list from glove mapping
        self.cocktails = {}

        
    def _get_key_words(self,query): # extracts keywords from query
        s = set(stopwords.words('english'))
        sp = set(['I'])
        self.query = [w for w in query.lower().split() if w not in s]

        
    def stem_phrase(self,phrase):
        token_words = word_tokenize(phrase)
        stemmed_phrase = []
        for word in token_words:
            stemmed_phrase.append(lancaster.stem(word))
        return stemmed_phrase
        
        
    def search_comments(self,query): # This does a direct search on variations of key word and returns cocktails'
        self._get_key_words(query)
        d = defaultdict(int)
        for item in self.query:
            test_word = lancaster.stem(item)
            for key in cocktails.keys():
                comment = cocktails[key]['comments']
                ingredients = cocktails[key]['ingredients']
                stem_list = self.stem_phrase(comment)
                stem_title = self.stem_phrase(key)
                ing_list = [self.stem_phrase(ingredient) for ingredient in cocktails[key]['ingredients']]
                stem_ingredients = [item for sublist in ing_list for item in sublist]
                if test_word in stem_list or test_word in stem_title or test_word in stem_ingredients:
                    d[key] += stem_list.count(test_word)
                    d[key] += stem_ingredients.count(test_word)*2
                    d[key] += stem_title.count(test_word)*2 # Doubled score if word is in title
        cocktail_dict = {k: v for k, v in sorted(d.items(), key=lambda item: item[1],reverse=True)}
        cocktail_list = list(cocktail_dict.keys())
        filtered_dict = {}
        for item in cocktail_list:
            filtered_dict[item] = cocktails[item]
        self.cocktails.update(filtered_dict)
    
    
    # helper function that returns for one word:
    def glove_score(self,word):
        d = {}
        ingredient_list = [item for item in ingredient_dict.keys() if ingredient_dict[item]['category'] in ('spirit','liqueur')]
        for item in ingredient_list:
            try:
                d[item] = np.mean([spatial.distance.euclidean(embedding_dict[ele],embedding_dict[word]) for ele in item.split()])
            except: 
                d[item] = 100
        return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
    
    
    # helper function:
    def glove_to_ingredients(self,query):
        self._get_key_words(query)
        d = Counter()
        for word in self.query:
            d += Counter(self.glove_score(word))
        self.ingr_list = list(d.keys())[:5]
        return self.ingr_list
    
    
    # Main function to find 5 closest cocktails based on ingredient mapping:
    def ingredients_to_cocktails(self,query):
        self.glove_to_ingredients(query)
        ind = [categories.index(item) for item in self.ingr_list] # indicies of cur_list ingredients
        # Get similarity matrix:
        A = np.zeros([len(cocktails)+1,len(categories)],dtype=int)
        for row,key in enumerate(cocktails): # loop through cocktails
            a = cocktails[key]['category']
            index = [i for i,x in enumerate(categories) if x in a]
            A[row,index] = np.ones([1,len(index)])

        A[-1,ind] = 1 # Fill ingredients of test cocktail

        # Similarity Matrix: 
        cocktail_list = [keys for keys in cocktails]
        similarity_matrix = cosine_similarity(A)
        np.fill_diagonal(similarity_matrix,0) # fill diagonal with zeros
        # Returns most similar cocktails:
        ord_idx = similarity_matrix.argsort()[-1,-5:][::-1]
        cocktail_list  = [cocktail_list[item] for item in ord_idx]
        filtered_dict = {}
        for item in cocktail_list:
            filtered_dict[item] = cocktails[item]
        self.cocktails.update(filtered_dict)