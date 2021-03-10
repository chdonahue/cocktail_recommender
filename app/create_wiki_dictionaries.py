# This script creates a dictionaries of Wikipedia data for all ingredients in each of the 5 different categories: 
# (spirits, liqueurs, juices, syrups, and other). This will be used for a training set with reddit data. 

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import dill
import os


# List of Cocktail ingredients that are used to train the models:
spirit_list = ['bourbon','brandy', 'gin', 'mezcal','rum', 'tequila', 'vodka', 'whiskey','cachaca','absinthe']

liqueur_list = ['orange liqueur','cherry liqueur','chocolate liqueur','bénédictine','amaro','campari','yellow chartreuse',
                'st. germain','green chartreuse','apricot liqueur','apple liqueur','coffee liqueur','amaretto','galliano',
                'falernum','aperol','peach liqueur','cynar','crème de menthe','fernet','allspice liqueur','crème yvette',
                'irish cream','passion fruit liqueur','schnapps','crème de cassis','strega','ouzo'] 

juice_list = ['lime juice','lemon juice','orange juice','pineapple juice','grapefruit juice','apple juice','tomato juice',
              'watermelon juice','passion fruit juice'] # Juices

syrup_list = ['simple syrup','grenadine','honey syrup','orgeat','cinnamon bark syrup','ginger syrup',
             'maple syrup','vanilla syrup','agave syrup'] # Syrups

other_list = ['egg','beer','hot sauce','coffee','heavy cream',
             'coconut milk','milk']



# This mapping was hard-coded to find the correct Wikipedia URLs:
# Hard-code some of the non-standard mappings: 
ingr_url_dict = {
    'bourbon': ['Bourbon_whiskey'],
    'orange liqueur': ['cointreau','Curaçao_(liqueur)','Grand_Marnier','Triple_sec'],
    'cherry liqueur': ['Maraschino'],
    'benedictine': ['Bénédictine'],
    'amaro': ['Amaro_(liqueur)'],
    'yellow chartreuse': ['Chartreuse_(liqueur)'],
    'green chartreuse': ['Chartreuse_(liqueur)'],
    'apricot liqueur':['apricot'], # mapped to the fruit
    'apple liqueur': ['Applejack_(drink)','Calvados'],
    'coffee liqueur': ['Kahlúa'],
    'galliano': ['Galliano_(liqueur)'],
    'peach liqueur': ['peach'],
    'allspice liqueur': ['allspice'],
    'irish cream': ['Baileys_Irish_Cream','Irish_cream'],
    'passion fruit liqueur': ['Passion_fruit_(fruit)','Passoã'],
    'crème yvette': ['Creme_Yvette'],
    'crème de noyaux': ['Crème_de_Noyaux'],
    'crème de ananas': ['pineapple'],
    'crème de banana': ['banana'],
    'suze': ['Suze_(drink)'],
    'midori': ['Midori_(liqueur)'],
    'strega': ['Strega_(liqueur)'],
    'st. germain': ['St-Germain_(liqueur)'],
    'picon': ['Picon_(apéritif)'],
    'arak': ['Arak_(drink)'],
    'génépy des alpes': ['Génépi'],
    'lime juice': ['Lime_(fruit)'],
    'orange juice': ['Orange_juice'],
    'tomato juice': ['Tomato_juice'],
    'apple juice': ['Apple_juice'],
    'grapefruit juice': ['Grapefruit_juice'],
    'pineapple juice': ['Pineapple_juice'],
    'lemon juice': ['lemon'],
    'watermelon juice': ['Watermelon'],
    'passion fruit juice': ['Passion_fruit_(fruit)'],
    'simple syrup': ['sugar'],
    'honey syrup': ['honey'],
    'orgeat': ['Orgeat_syrup'],
    'cinnamon bark syrup': ['Cinnamon'],
    'ginger syrup': ['Ginger'],
    'maple syrup': ['Maple_syrup'],
    'vanilla syrup': ['Vanilla'],
    'agave syrup': ['Agave_syrup'],
    'hot sauce': ['Hot_sauce'],
    'heavy cream': ['cream'],
    'coconut milk': ['Coconut_milk']
}


# Ingredients -> URL Mapping:
base_url = "http://en.wikipedia.org/wiki/"
def ingredients_to_urls(ingredient_list):
    """
    Take list of ingredients and return valid wikipedia url dictionary
    """
    d = {}
    for ele in ingredient_list:
        L = []
        if ele in ingr_url_dict:
            items = ingr_url_dict[ele]
        else:
            items = [ele]
        for item in items:
            url = base_url+item
            L.append(url.replace(' ','_'))
        d[ele] = L
    return d



# Get URL MAPPINGS for each category:
spirit_urls = ingredients_to_urls(spirit_list)
liqueur_urls = ingredients_to_urls(liqueur_list)
juice_urls = ingredients_to_urls(juice_list)
syrup_urls = ingredients_to_urls(syrup_list)
other_urls = ingredients_to_urls(other_list)


# Retrieve Wikipedia data from URLs:
def wikipedia_to_paragraphs(url):
    """
    Retrieves a URL from wikipedia, and returns a list of paragraphs 
    (based on the 'p' html paragraph tag) 
    """
    r = requests.get(url)
    page_text = r.text.encode('utf-8').decode('ascii', 'ignore')
    soup = BeautifulSoup(page_text).find(attrs={'id':'mw-content-text'})
    
    # The text is littered by references like [n].  Drop them.
    def drop_refs(s):
        return ''.join( re.split('\[\d+\]', s) )
    
    return [drop_refs(p.text) for p in soup.find_all('p') if p.text != '']



# Create a Dictionary for a given Category:
def wiki_to_dictionary(urls):
	d = {}
	for k,v in urls.items():
		d[k] = []
		for url in v:
			d[k].extend(wikipedia_to_paragraphs(url))
	return d



# Create separate dictionaries:
spirit_wiki = wiki_to_dictionary(spirit_urls)
liqueur_wiki = wiki_to_dictionary(liqueur_urls)
juice_wiki = wiki_to_dictionary(juice_urls)
syrup_wiki = wiki_to_dictionary(syrup_urls)
other_wiki = wiki_to_dictionary(other_urls)

if not os.path.exists('model_data'):
	os.mkdir('model_data')





# Save wikipedia data:
dill.dump(spirit_wiki, open('model_data/spirit_wiki.pkd', 'wb'))
dill.dump(liqueur_wiki, open('model_data/liqueur_wiki.pkd', 'wb'))
dill.dump(juice_wiki, open('model_data/juice_wiki.pkd', 'wb'))
dill.dump(syrup_wiki, open('model_data/syrup_wiki.pkd', 'wb'))
dill.dump(other_wiki, open('model_data/other_wiki.pkd', 'wb'))