from flask import Flask, render_template, request, redirect, jsonify
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from CocktailMap import CocktailMap
import time
app = Flask(__name__)


class DataStore():
	a = None

data = DataStore()


@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		query = request.form['query']
		C = CocktailMap(query)
		f = C.plot_cocktail_map(20).to_json()
		cocktails = C.cocktails
		data.a = cocktails
		return render_template('index.html',chart_json=f,query=query,cocktails=cocktails)
	return render_template('index.html')


@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/<variable>')
def get_recipe(variable):
	cocktails = data.a
	if data.a is None: # kluge to deal with race problem
		time.sleep(1)

	return render_template("recipe_template.html",drink = cocktails[variable])




if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)


	# app.run(port=33507,debug=True) # Debug mode
