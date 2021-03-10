# import sys
# sys.path.append("/Users/christopherdonahue/Documents/GitHub/bartender/")
# import pickle
from flask import Flask, render_template, request, redirect, jsonify
import requests
import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure
from Bar import Cocktails, Word2Cocktail
from bartender_mappings import ingredient_dict


app = Flask(__name__)


# Some stuff to organize later: THIS ORDERS INGREDIENTS BY FREQUENCY
def get_ingredient_freq(cocktail_dict):
    ingred_count = {}
    for key in cocktail_dict:
        for ingred in cocktail_dict[key]['category']: 
            if ingred in ingred_count.keys():
                ingred_count[ingred]+=1
            else:
                ingred_count[ingred] = 1
    # Sorted dictionary with frequencies:            
    return {k: v for k, v in sorted(ingred_count.items(), key=lambda item: item[1],reverse=True)}   
# TEST Recipe page:
my_bar = Cocktails() # instantiate Cocktails object
cocktail_dict = my_bar.all_cocktails
ingred_freq = get_ingredient_freq(cocktail_dict)
# my_bar.add_ingredients(['simple syrup','orange liqueur','mezcal','tequila','gin','rum',
# 	'lime juice','lemon juice','aperol','campari','orange bitters','vermouth','diary','soda','fernet',
# 	'elderflower','soy sauce','amaro','st-germain','strawberry','worcestershire','fruit','apricot liqueur',
# 	'cinnamon bark syrup','pineapple juice'])


# Testing out ingredients for populating refactor.html:
ingredient_test = {}
spirits = [key for key in ingredient_dict.keys() if ingredient_dict[key]['category']=='spirit']
spirits = [key for key in ingred_freq.keys() if key in spirits]
liqueurs = [key for key in ingredient_dict.keys() if ingredient_dict[key]['category']=='liqueur']
liqueurs = [key for key in ingred_freq.keys() if key in liqueurs]
juice = [key for key in ingredient_dict.keys() if ingredient_dict[key]['category']=='juice']
juice = [key for key in ingred_freq.keys() if key in juice]
syrup = [key for key in ingredient_dict.keys() if ingredient_dict[key]['category']=='syrup']
syrup = [key for key in ingred_freq.keys() if key in syrup]
wine = [key for key in ingredient_dict.keys() if ingredient_dict[key]['category']=='wine']
wine = [key for key in ingred_freq.keys() if key in wine]
spices = [key for key in ingredient_dict.keys() if ingredient_dict[key]['category']=='spices and herbs']
spices = [key for key in ingred_freq.keys() if key in spices]
ingredient_test['spirits'] = spirits
ingredient_test['liqueurs'] = liqueurs
ingredient_test['juice'] = juice
ingredient_test['syrup'] = syrup
ingredient_test['wine'] = wine
ingredient_test['spices'] = spices


@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		Cktl = Word2Cocktail()
		query = request.form['query']
		Cktl.search_comments(query)
		# print(len(Cktl.cocktails))
		# if len(Cktl.cocktails)==0:
		Cktl.ingredients_to_cocktails(query)
		return render_template('recipe_list.html',cocktails=Cktl.cocktails)
	return render_template('index.html')

@app.route('/answer_page')
def answer_page():
	
	return render_template('answer_page.html')


@app.route('/refactor2',methods=['GET','POST'])
def refactor():
	if request.method == 'POST':
		b = Cocktails()
		new_ingredients = request.form['submit_button']
		b.add_ingredients(new_ingredients.split(','))
		print(b.my_cocktails)
		return render_template('recipe_list.html',cocktails=b.my_cocktails)
	return render_template('refactor2.html',ingredients = ingredient_test)


@app.route('/recipe_list')
def recipe_list():
	return render_template('recipe_list.html',cocktails=my_bar.my_cocktails)

@app.route('/<variable>')
def get_recipe(variable):
	return render_template("recipe_template.html",drink=my_bar.all_cocktails[variable])


# @app.route('/jquery_test')
# def jquery_test():
# 	return render_template('jquery_test.html')

# @app.route('/jquery_tutorial')
# def jquery_tutorial():
# 	return render_template('jquery_tutorial.html')	

# @app.route('/jqueryUI_tutorial')
# def jqueryUI_tutorial():
# 	return render_template('jqueryUI_tutorial.html')	

# @app.route('/menu_test',methods=['GET','POST'])
# def menu_test():
# 	if request.method == 'POST':
# 		print(request.form['submit_button'])
# 	elif request.method == 'GET':
# 		return render_template('menu_test.html',ingredients = ingredient_test)



# This is a test and will be removed later:
# @app.route('/recipe')
# def recipe():
# 	return render_template('recipe.html',len=len(this_drink['ingredients']),drink=this_drink)

if __name__ == '__main__':
  app.run(port=33507,debug=True)
