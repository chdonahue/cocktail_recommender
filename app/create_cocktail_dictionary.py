# This creates a master dictionary with all important info
import pickle
import re
from bartender_mappings import ingredient_dict, measure_dict

# Unpickle raw data:
with open("raw_drinks.pickle", "rb") as file:
    drinks = pickle.load(file)


search_terms = [item for key in ingredient_dict.keys() for item in ingredient_dict.get(key).get('search_terms')]


# helper functions: 
def get_key(val):
    for ingredient in ingredient_dict.keys():
        if val in ingredient_dict[ingredient]['search_terms']:
            return ingredient
    return None

def get_categories(ingredients):
    ingr = list()
    for num,ingredient in enumerate(ingredients):
        ingr.insert(num,'')
        for ele in search_terms:
            if re.findall('\\b'+ele+'\\b',ingredient.lower()):
                ingr[num] = get_key(ele)
                break
    return ingr

# Parse quantities and convert all to ounces:
def get_quantities(ingredients):
    measures = list(measure_dict.keys())
    skip_words = ['garnish','peel','slice','slices']
    quant = list() # list of quantities converted to ounces
    for num,ingredient in enumerate(ingredients):
        # Quantity:
        try:
            q = float(ingredient.split()[0])
        except:
            q = None
            try:
                q = float(ingredient.split()[1]) # rare cases it is 2nd element
            except:
                q = None


        # Get measures:
        temp = set(ingredient.lower().split())
        idx = [i for i, val in enumerate(measures) if val in temp] # idx in measures
        if idx:
            m = measures[idx[0]]
        else:
            m = None 

        # take care of special cases:
        if any(item in ingredient.lower() for item in ['angostura','bitters']) and not q: 
            m = 'dash'
            q = 1
        if any(item in ingredient.lower() for item in ['champagne','soda']) and not q: 
            m = 'float'
            q = 1
        if any(item in ingredient.lower() for item in ['cinnamon']) and not q: 
            m = 'pinch'
            q = 1
        if any(item in ingredient.lower() for item in ['dash']): 
            q = 1
        if any(item in ingredient.lower() for item in skip_words):
            m = None
            q = None        
        if not m or not q: # take care of a few rare cases where perhaps a muddle or garnish is added
            m = None
            q = None
        if m in measure_dict: # transform to ounces
            quant.append(q*measure_dict[m])
        else:
            quant.append(None)
    return quant

def add_author(source,comments): # Function to add author:
    if source=="The Craft of the Cocktail":
        return "Dale DeGroff"
    elif source=="PDT":
        return "Jim Meehan"
    elif source=="Death & Co":
        substr = re.split('\n|,',comments)
        return (''.join([char for char in substr if char.isupper()]).title())

def add_style(instructions,comments): # Function to add style: shaken or stirred? 
    if any(x in instructions+comments for x in ["stir","combine","mix","pour","swizzle","build"]):
        return 'stirred'
    if any(x in instructions+comments for x in ["shake","shaking"]):
        return 'shaken'
    if any(x in instructions+comments for x in ["blend"]):
        return 'blended'
    if any(x in instructions+comments for x in ["layer"]):
        return 'layered'



# Put drinks into dictionary format:
new_drinks = dict()
for book_num in range(len(drinks)):
    for drink_num in range(len(drinks[book_num])):
        source = drinks[book_num][drink_num]['source']
        comments = drinks[book_num][drink_num]['comments']
        instructions = drinks[book_num][drink_num]['instructions'].lower()
        ingredients = drinks[book_num][drink_num]['ingredients']
        drinks[book_num][drink_num]['category'] = get_categories(ingredients)
        drinks[book_num][drink_num]['quantity'] = get_quantities(ingredients)
        drinks[book_num][drink_num]['author'] = add_author(source,comments)
        drinks[book_num][drink_num]['style'] = add_style(instructions,comments)
        # TBD: add glassware and other useful elements in the future
        new_drinks[drinks[book_num][drink_num]['cocktail_name']] = drinks[book_num][drink_num]



# Pickle new data:
with open("cocktails.pickle", "wb") as file:
	pickle.dump(new_drinks, file)

