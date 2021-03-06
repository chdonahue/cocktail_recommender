# COCKTAIL RECOMMENDER PROJECT

<img src="/app/img/barman-behind-bar.jpg" />

I love craft cocktails, but during COVID I wasn't able to go out and enjoy them. During the lockdown, I decided to learn how to make my own cocktails. I bought a great cocktail book [DEATH & CO](https://www.amazon.com/Death-Co-Modern-Classic-Cocktails/dp/1607745259) and built up my home bar. 

One thing I miss is being able to interact with a bartender and describe in vague terms what kind of cocktail I want. For example I can ask, **"Do you have anything kinda smoky but spicy?"** A good bartender can come up with a good cocktail to match. I wanted to train a model to do this for me. 


## BUILDING A MODEL TO MAP QUERIES TO COCKTAILS
For this project, I decided to build a model that uses NLP to rank cocktails that match a user's query. 

**STEPS:**

1. Get the data
2. Extract ingredient categories for the cocktails
3. Build the training set from Wikipedia and subreddit data
4. Train the model and visualize results
    

## GETTING THE DATA
The most important thing for me was to find a good source of creative cocktail recipes (no Cosmos messing up my dataset!). 
I found a great site upneat.rocks that had exactly what I was looking for. All cocktails from 3 famous craft cocktail books, including Death & Co! 

I used Beautiful Soup (code in <b>upneat_scraper.py</b>) to extract all the contents



## EXTRACTING INGREDIENTS
Ingredients had to be abstracted into categories for this to work. As seen in the example below, brand names are often found in the recipes (<em>i.e. Siembra Azul Blanco Tequila</em>) and I want this to simply be <em>Tequila</em>. This was somewhat arbitrary, but I managed to extract around 160 unique ingredients from the cocktail database. 

**GILDA COCKTAIL**
- 2 ounces Siembra Azul Blanco Tequila
- .5 ounce Pineapple Juice
- .5 ounce Lime Juice
- .5 ounce Cinnamon Bark Syrup
- Wheel of Lime (Garnish)


## BUILDING A TRAINING SET FROM WIKIPEDIA AND REDDIT DATA

I selected the most common ingredients and scraped Wikipedia and subreddits (when they existed) corresponding to these ingredients (code in <b>create_wiki_diciontaries.py</b> and <b>create_reddit_dictionaries.py</b>) 

Next, I separated all the ingredients into 5 general categories that cocktails tend to have:
1. Spirits (Rum, Tequila, etc.)
2. Juices (Lemon, Lime, etc.
3. Liqueurs (Triple Sec, Kahlua, etc.)
4. Syrups (Simple syrup, grenadine, etc.)
5. Misc (Coffee, cream, etc.)

For each of these 5 categories, I built a model using Scikit-Learn's TFID Vectorizer to discover which words tended to be more frequent for a given ingredient (code in **create_NLP_models.py**)


## DEMO (In TDI_Capstone notebook)


### The model finds the most likely ingredients that match a query. Afterwards, cosine similarity is used to determine the closest cocktails to this query. I combine these results with simpler search methods that look for the query in the cocktail description and ingredients. The end result is the top N cocktails projected onto a 2d map that was derived with [Multidimensional Scaling](https://en.wikipedia.org/wiki/Multidimensional_scaling) on the set of cocktail ingredients

*Example Query: "smoky daiquiri"*

<img src="/app/img/fig1.png" />


**JOVENCOURT DAIQUIRI**
- 2 ounces Barbancourt White Rum
- .25 ounce Del Maguey Vida Mezcal
- .75 ounce Lime Juice
- .75 ounce Simple Syrup

Shake all the ingredients with ice, then strain into a coupe. No garnish.

PHIL WARD, 2007 This cocktail was my first epiphany about using mezcal in a mixed drink. Doing so is common now, but nobody was mixing with it back then.???PW

### There is a method to get a score for each of the ingredients that were derived from the model:
<img src="/app/img/fig2.png" />
<img src="/app/img/fig3.png" />
