import spacy
import dill
import pickle
import altair as alt
from bartender_mappings import ingredient_dict
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd
import numpy as np
import re
porter = PorterStemmer()

# Preload stuff: 
drink_map_df = dill.load(open('model_data/drink_distance_mapping.pkd', 'rb'))
drinks = dill.load(open('cocktail_data/cocktails.pickle', 'rb'))
juice_model = dill.load(open('model_data/juice_model.pkd', 'rb'))
spirit_model = dill.load(open('model_data/spirit_model.pkd', 'rb'))
syrup_model = dill.load(open('model_data/syrup_model.pkd', 'rb'))
liqueur_model = dill.load(open('model_data/liqueur_model.pkd', 'rb'))
reddit_model = dill.load(open('model_data/reddit_model.pkd', 'rb'))
other_model = dill.load(open('model_data/other_model.pkd', 'rb'))




def get_model_distribution(model,X):
	"""
	Input model and test phrases and output probability distribution of labels 
	"""
	correction = 1/model.predict_proba(['asdfkljkdf']) # This normalizes the model with a junk string
	prob = (model.predict_proba(X)*correction)
	prob = (prob/np.sum(prob)).T
	d = dict(zip(model.classes_.flatten(),prob.flatten()))
	return d


nlp = spacy.load("en_core_web_sm")
def tokenize_lemma(text):
	return [w.lemma_.lower() for w in nlp(text)]


class CocktailQuery:
	def __init__(self,query):
		self.query = query
		self.query_tok = [' '.join(tokenize_lemma(query))]
		self.scores = self.get_scores()
		self.weights = self.get_weights()


	def get_scores(self):
		wiki_scores = get_model_distribution(spirit_model,self.query_tok) # Average reddit and wikipedia models
		reddit_scores = get_model_distribution(reddit_model,self.query_tok)
		# Get Spirit, Juice, Liqueur
		spirit_scores = {k: (wiki_scores.get(k,0)+reddit_scores.get(k,0))/2 for k in set(wiki_scores) & set(reddit_scores)}
		juice_scores = get_model_distribution(juice_model,self.query_tok)
		liqueur_scores = get_model_distribution(liqueur_model,self.query_tok)
		syrup_scores = get_model_distribution(syrup_model,self.query_tok)
		misc_scores = get_model_distribution(other_model,self.query_tok)
		d = {'spirit_scores':spirit_scores,
			'juice_scores':juice_scores,
			'liqueur_scores':liqueur_scores,
			'syrup_scores':syrup_scores,
			'misc_scores':misc_scores
			}
		return d

	def get_weights(self):
		"""
		Returns dictionary of weights for each ingredient given query. This is hard-coded for now, but can be adjusted
		to give different results
		"""
		w = [1,.5] # hard-coding weights for top two ingredients in each category
		weights = {}
		for k in self.scores.keys():
			sorted_tuples = sorted(self.scores[k].items(), key=lambda item: item[1],reverse=True)
			top_two = [x[0] for x in sorted_tuples if x[1]>(1.05/len(sorted_tuples))][:2]
			for i,ele in enumerate(top_two):
				weights[ele] = w[i]
		return weights

	def get_cocktail_comment_scores(self):
		"""
		Searches through drink comments and ingredients for query
		"""
		multiplier = .6 # this is an arbitrary number that gets added for each word match
		s = stopwords.words('english')
		s.append('cocktail')
		q = [w for w in self.query.lower().split() if w not in s]
		d = Counter()
		for key in drinks.keys():
			c = (key+drinks[key]['comments']+' '.join(drinks[key]['ingredients'])).lower().replace(',','')
			c_stemmed = []
			for word in c.split():
				c_stemmed.append(porter.stem(word))
			c_stem = ' '.join(c_stemmed)
			for word in q:
				if re.search(r'\b({0})\b'.format(porter.stem(word)),c_stem):
					d[key]+= multiplier
		sorted_tuples = sorted(d.items(), key=lambda item: item[1],reverse=True)
		return dict(sorted_tuples)

	def get_recipe(self,cocktail):
		"""
		Returns a formatted Recipe for a given cocktail
		"""
		c = drinks[cocktail]
		# Print to screen:
		print(cocktail.upper())
		for ingredient in drinks[cocktail]['ingredients']:
			print(ingredient)
		print(drinks[cocktail]['instructions'])
		print(drinks[cocktail]['comments'])


	def get_cocktail_scores(self,N):
		"""
		Returns N tuples (cocktail, score) of top cocktails for the query
		"""
		# Create matrix of Cocktails X Ingredients
		categories = list(ingredient_dict.keys()) # list of ingredients (combine rhum agricole and rum??)
		categories[categories.index('cachaça')] = 'cachaca'
		A = np.zeros([len(drinks),len(categories)],dtype=int)
		for row,key in enumerate(drinks): # loop through cocktails
			a = drinks[key]['category']
			index = [i for i,x in enumerate(categories) if x in a]
			A[row,index] = np.ones([1,len(index)])
		new_vec = np.zeros((1,A.shape[1]))
		for k,v in self.weights.items():
			ind = categories.index(k)
			new_vec[0,ind] = v
		test = np.concatenate((new_vec,A),axis=0)
		cocktail_list = ['_target']
		cocktail_list.extend([keys for keys in drinks])
		similarity_matrix = np.around(cosine_similarity(test),decimals=2)
		np.fill_diagonal(similarity_matrix,0) # fill diagonal with zeros
		d = dict(zip(cocktail_list,similarity_matrix[0,:]))
		d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1],reverse=True)}
		s_d = self.get_cocktail_comment_scores()
		combined_dict = {k: d.get(k, 0) + s_d.get(k, 0) for k in set(d)}
		sorted_tuples = sorted(combined_dict.items(), key=lambda item: item[1],reverse=True)
		return sorted_tuples[:N]

	def plot_ingredient_scores(self,item):
		"""
		item can be ('spirits','juices','liqueurs','misc','syrups')
		"""
		liqueur_labels = [ele.replace('liqueur','') for ele in self.scores['liqueur_scores'].keys()]
		syrup_labels = [ele.replace('syrup','') for ele in self.scores['syrup_scores'].keys()]
		misc_labels = list(self.scores['misc_scores'].keys())
		juice_labels = [ele.replace('juice','') for ele in self.scores['juice_scores'].keys()]
		spirit_labels = list(self.scores['spirit_scores'].keys())
		data_dict = {'liqueurs':[liqueur_labels,self.scores['liqueur_scores']],
					 'syrups': [syrup_labels,self.scores['syrup_scores']],
					 'juices': [juice_labels,self.scores['juice_scores']],
					 'spirits': [spirit_labels,self.scores['spirit_scores']],
					 'misc': [misc_labels,self.scores['misc_scores']]
					}
		data = {item: data_dict[item][0],
			'score': list(data_dict[item][1].values()),
			'col': [y>(1.05/len(data_dict[item][1].keys())) for x,y in data_dict[item][1].items()]}
		source = pd.DataFrame.from_dict(data)
		plot = alt.Chart(source).mark_bar().encode(
		    x= item,
		    y= 'score',
		    color = alt.Color('col', legend=None),
		    tooltip=[item,'score']
		    ).properties(
		        title = item.upper(),
		        height=300,
		        width=500
		    ).configure_axis(
		        labelFontSize=20,
		        titleFontSize=20
		    ).configure_title(
		        fontSize=25
		    )
		return(plot)   
    
    
	def plot_cocktail_map(self,N):
		"""
		Multidimensional scaling map to plot top N cocktails
		"""
		hover = alt.selection_single(empty='all')#, fields=['cocktail'])

		subset_df = pd.DataFrame(self.get_cocktail_scores(N), columns=['cocktail','score'])
		new_df = pd.merge(subset_df,drink_map_df)
		new_df = new_df[new_df['score']>0]
		chart1 = alt.Chart(new_df).mark_point(filled=True,size=150,stroke='black'
		).encode(
		    x='x',
		    y='y',
		    color = 'style',
		    tooltip=['cocktail','ingredients','style','score']
		).properties(
		    title = 'COCKTAIL MATCHES',
		    height=450,
		    width=450
		).interactive(
		)


		# Base chart for data tables
		ranked_text = alt.Chart(new_df).mark_text(fontSize=14).encode(
		    y=alt.Y('row_number:O',axis=None)
		).transform_window(
		    row_number='row_number()'
		).properties(width=150)

		chart2 = alt.Chart(drink_map_df).mark_point(size=2).encode(x='x',y='y',color='style')

		plot = (chart1+chart2)


		# Data Table
		cocktail_tab = ranked_text.encode(text='cocktail',tooltip=['ingredients','style']).properties(title='cocktail')
		score_tab = ranked_text.encode(text='score').properties(title='score')
		text = alt.hconcat(cocktail_tab,score_tab).add_selection(hover) # Combine data tables
		plot = alt.hconcat(
		    plot,
		    text
		).resolve_legend(color='independent'
		).configure_view(
		    strokeWidth=0
		).configure_axis(
		    labelFontSize=18,
		    titleFontSize=18
		).configure_title(
		    fontSize=25
		).configure_legend(
		    titleFontSize=15,
		    labelFontSize=12
		)

		return plot