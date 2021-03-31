from flask import Flask, render_template, request, redirect, jsonify, session
from flask_session.__init__ import Session
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from CocktailMap import CocktailMap
app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)



@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		query = request.form['query']
		C = CocktailMap(query)
		f = C.plot_cocktail_map(20).to_json()
		session['data'] = C.cocktails
		return render_template('index.html',chart_json=f,query=query,cocktails=C.cocktails)
	return render_template('index.html')


@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/<variable>')
def get_recipe(variable):
	cocktails = session['data']
	return render_template("recipe_template.html",drink = cocktails[variable])

# Add example pages for about page: 
@app.route('/Stolen%20Huffy')
def show_huffy():
	return render_template("huffy.html")

@app.route('/Gilda%20Cocktail')
def show_gilda():
	return render_template("gilda.html")

@app.route('/Jovencourt%20Daiquiri')
def show_jovencourt():
	return render_template("jovencourt.html")


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)


	# app.run(port=33507,debug=True) # Debug mode
