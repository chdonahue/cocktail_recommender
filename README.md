# cocktail_recommender

# COCKTAIL RECOMMENDER PROJECT

I love craft cocktails, but during COVID I wasn't able to go out and enjoy them. During the lockdown, I decided to learn how to make my own cocktails. I bought a great cocktail book [DEATH & CO](https://www.amazon.com/Death-Co-Modern-Classic-Cocktails/dp/1607745259) and built up my home bar. 

One thing I miss is being able to interact with a bartender and describe in vague terms what kind of cocktail I want. For example I can ask, **"Do you have anything kinda smoky but spicy?"** A good bartender can come up with a good cocktail to match. 



## GETTING THE DATA
The most important thing for me was to find a good source of creative cocktail recipes (no Cosmos messing up my dataset!). 
I found a great site upneat.rocks that had exactly what I was looking for. All cocktails from 3 famous craft cocktail books, including Death & Co! 

I used Beautiful Soup (code in <b>upneat_scraper.py</b>) to extract all the contents


## EXTRACT INGREDIENTS
Ingredients had to be abstracted into categories for this to work. As seen in the example below, brand names are often found in the recipes (<em>i.e. Siembra Azul Blanco Tequila</em>) and I want this to simply be <em>Tequila</em>. This was somewhat arbitrary, but I managed to extract around 160 unique ingredients from the cocktail database. 
