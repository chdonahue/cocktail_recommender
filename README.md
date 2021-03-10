# cocktail_recommender

# COCKTAIL RECOMMENDER PROJECT
<h1><center>BUILT FOR AMATEUR MIXOLOGISTS</center></h1>

I love craft cocktails, but during COVID I wasn't able to go out and enjoy them. During the lockdown, I decided to learn how to make my own cocktails. I bought a great cocktail book [DEATH & CO](https://www.amazon.com/Death-Co-Modern-Classic-Cocktails/dp/1607745259) and built up my home bar. 

One thing I miss is being able to interact with a bartender and describe in vague terms what kind of cocktail I want. For example I can ask, **"Do you have anything kinda smoky but spicy?"** A good bartender can come up with a good cocktail to match. 
**TODO:** 
- Work on catching all missed mappings (working on this in bar_sandbox.ipynb)
  - also, some basic errors with needing to search for exact strings! 
- Add other features: author, quantities, measures

### Cocktails object:
Bar.py contains a Cocktails object which has some basic built-in features:
- Add ingredients to your bar (Cocktails.add_ingredients) and it maintain a list of possible cocktails you can make given what you have
- Display recipes (Cocktails.display_recipes) will display all the recipes with instructions given your ingredient list

**TODO:** 
- Create tkinter object to allow nicely formatted and interactive cocktail menus
- Once I fix some data cleaning issues (quantities, ingredient categories), do some EDA to look at cocktail features. This will help me eventually create a recommender and cocktail creator
  - Create a metric to determine distance between drinks
- Add functionality to rate cocktails
- Build in substitutes mappings so ingredient substitutions are recommended (this could also help AI find similar cocktails or invent subtle variations on old ones)
- Allow users through a tkiniter app to add their own unique cocktails
- Unsupervised methods for clustering recipes based on how often ingredients are combined (I'm thinking of something analagous to a flavor bible for mixology)



