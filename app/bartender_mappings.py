# This contains data that will be used by create_updated_list.py to map ingredient strings to categories
# it is being worked on in bar_sandbox.ipynb right now

# Put into list
# ingredient_cat_list_ = [item.lower() for sublist in list(ingredient_mappings_.values()) for item in sublist]


ingredient_dict = {}
# SPIRITS:
ingredient_dict['rhum agricole'] = {'category':'spirit',
            'search_terms': ['rhum','agricole'],
            'substitutions': ['rum','white rum']}

ingredient_dict['rum'] = {'category':'spirit',
            'search_terms': ['rum','bacardi'],
            'substitutions': ['rhum','white rum']}

ingredient_dict['arrack'] = {'category':'spirit',
            'search_terms': ['batavia arrack','arrack'],
            'substitutions': ['rum','rhum']}

ingredient_dict['white rum'] = {'category':'spirit',
            'search_terms': ['white rum'],
            'substitutions': ['rhum','rum']}

ingredient_dict['cachaça'] = {'category':'spirit',
            'search_terms': ['cachaça'],
            'substitutions': ['white rum']}

ingredient_dict['tequila'] = {'category':'spirit',
                'search_terms': ['tequila','cuervo'],
                'substitutions': ['mezcal']}

ingredient_dict['mezcal'] = {'category':'spirit',
                'search_terms': ['mezcal'],
                'substitutions': ['tequila']}

ingredient_dict['gin'] = {'category':'spirit',
                'search_terms': ['gin'],
                'substitutions': []}

ingredient_dict['bols genever'] = {'category':'spirit',
                'search_terms': ['bols genever'],
                'substitutions': ['gin']}

ingredient_dict['whiskey'] = {'category':'spirit',
                'search_terms': ['whisky','whiskey','southern comfort'],
                'substitutions': ['bourbon']}

ingredient_dict['bourbon'] = {'category':'spirit',
                'search_terms': ['bourbon'],
                'substitutions': ['whiskey']}

ingredient_dict['vodka'] = {'category':'spirit',
                'search_terms': ['vodka'],
                'substitutions': []}

ingredient_dict['absinthe'] = {'category':'spirit',
                'search_terms': ['absinthe'],
                'substitutions': ['anise liqueur']}

ingredient_dict['metaxa'] = {'category':'spirit',
                'search_terms': ['metaxa'],
                'substitutions': ['brandy']}

ingredient_dict['brandy'] = {'category':'spirit',
                'search_terms': ['brandy','cognac','armagnac','kirschwasser','kirsch','pear brandy','pineau des charentes'],
                'substitutions': []}

ingredient_dict['pisco'] = {'category':'spirit',
                'search_terms': ['pisco'],
                'substitutions': ['brandy']}

ingredient_dict['aquavit'] = {'category':'spirit',
                'search_terms': ['aquavit'],
                'substitutions': []}

ingredient_dict['soju'] = {'category':'spirit',
                'search_terms': ['soju','bek se ju'],
                'substitutions': ['vodka']}




# LIQUEURS:
ingredient_dict['orange liqueur'] = {'category':'liqueur',
                'search_terms': ['orange liqueur','cointreau','creole shrub','créole shrubb','grand marnier','curaçao','triple sec',\
                        'royal combier','napoléon liqueur','élixir combier'],
                'substitutions': []}

ingredient_dict['strawberry liqueur'] = {'category':'liqueur',
                'search_terms': ['strawberry liqueur'],
                'substitutions': [],
                'instructions': 'https://www.seriouseats.com/recipes/2012/06/homemade-strawberry-liqueur-recipe.html'}

ingredient_dict['schnapps'] = {'category':'liqueur',
                'search_terms': ['schnapps'],
                'substitutions': []}

ingredient_dict['swedish punsch'] = {'category':'liqueur',
                'search_terms': ['swedish punsch','flaggpunsch'],
                'substitutions': []}

ingredient_dict['amaretto'] = {'category':'liqueur',
                'search_terms': ['amaretto'],
                'substitutions': ['crème de noyaux']}

ingredient_dict['falernum'] = {'category':'liqueur',
                'search_terms': ['falernum'],
                'substitutions': []}

ingredient_dict['drambuie'] = {'category':'liqueur',
                'search_terms': ['drambuie','irish mist'],
                'substitutions': ['whiskey']}

ingredient_dict['crème yvette'] = {'category':'liqueur',
                'search_terms': ['crème yvette','parfait amour'],
                'substitutions': ['crème de violette']}

ingredient_dict['crème de violette'] = {'category':'liqueur',
                'search_terms': ['crème de violette',],
                'substitutions': ['crème yvette']}

ingredient_dict['crème de noyaux'] = {'category':'liqueur',
                'search_terms': ['crème de noyaux'],
                'substitutions': ['amaretto']}

ingredient_dict['frangelico'] = {'category':'liqueur',
                'search_terms': ['frangelico'],
                'substitutions': ['amaretto','crème de noyaux','coffee liqueur']}

ingredient_dict['kumquat liqueur'] = {'category':'liqueur',
                'search_terms': ['kumkwat cordial','kumquat cordial','kumquat liqueur'],
                'substitutions': []}

ingredient_dict['cranberry liqueur'] = {'category':'liqueur',
                'search_terms': ['cranberry cordial','cranberry liqueur'],
                'substitutions': []}

ingredient_dict['black currant liqueur'] = {'category':'liqueur',
                'search_terms': ['black currant cordial','black currant liqueur'],
                'substitutions': []}

ingredient_dict['irish cream'] = {'category':'liqueur',
                'search_terms': ['irish cream','baileys'],
                'substitutions': []}

ingredient_dict['banana liqueur'] = {'category':'liqueur',
                'search_terms': ['banana liqueur'],
                'substitutions': ['crème de ananas']}

ingredient_dict['pomegranate liqueur'] = {'category':'liqueur',
                'search_terms': ['pomegranate liqueur'],
                'substitutions': []}

ingredient_dict['chocolate liqueur'] = {'category':'liqueur',
                'search_terms': ['chocolate liqueur','godiva','crème de cacao'],
                'substitutions': ['coffee liqueur']}

ingredient_dict['coffee liqueur'] = {'category':'liqueur',
                'search_terms': ['kahlúa','coffee liqueur'],
                'substitutions': []}

ingredient_dict['galliano'] = {'category':'liqueur',
                'search_terms': ['galliano'],
                'substitutions': ['ouzo']}

ingredient_dict['apricot liqueur'] = {'category':'liqueur',
                'search_terms': ['apricot liqueur','brizard apry'],
                'substitutions': ['pear liqueur','peach liqueur']}

ingredient_dict['peach liqueur'] = {'category':'liqueur',
                'search_terms': ['peach liqueur','pêche liqueur'],
                'substitutions': ['pear liqueur','apricot liqueur']}

ingredient_dict['walnut liqueur'] = {'category':'liqueur',
                'search_terms': ['walnut liqueur'],
                'substitutions': []}

ingredient_dict['crème de ananas'] = {'category':'liqueur',
                'search_terms': ['crème de ananas'],
                'substitutions': []}

ingredient_dict['crème de menthe'] = {'category':'liqueur',
                'search_terms': ['crème de menthe'],
                'substitutions': []}

ingredient_dict['crème de banana'] = {'category':'liqueur',
                'search_terms': ['crème de banane','crème de banana'],
                'substitutions': []}

ingredient_dict['pear liqueur'] = {'category':'liqueur',
                'search_terms': ['pear liqueur'],
                'substitutions': ['brandy','apricot liqueur','apple liqueur','peach liqueur']}

ingredient_dict['vanilla liqueur'] = {'category':'liqueur',
                'search_terms': ['tuaca','vanilla liqueur','licor 43'],
                'substitutions': []}

ingredient_dict['apple liqueur'] = {'category':'liqueur',
                'search_terms': ['calvados','apple liqueur','applejack'],
                'substitutions': ['brandy','apricot liqueur','pear liqueur']}

ingredient_dict['cherry liqueur'] = {'category':'liqueur',
                'search_terms': ['cherry liqueur','maraschino liqueur','cherry heering'],
                'substitutions': ['brandy']}

ingredient_dict['blackberry liqueur'] = {'category':'liqueur',
                'search_terms': ['blackberry liqueur'],
                'substitutions': ['brandy','raspberry liqueur','crème de cassis']}

ingredient_dict['raspberry liqueur'] = {'category':'liqueur',
                'search_terms': ['raspberry liqueur','chambord','framboise'],
                'substitutions': ['brandy','blackberry liqueur','crème de cassis']}

ingredient_dict['crème de cassis'] = {'category':'liqueur',
                'search_terms': ['crème de cassis'],
                'substitutions': ['raspberry liqueur','blackberry liqueur']}

ingredient_dict['grapefruit liqueur'] = {'category':'liqueur',
                'search_terms': ['grapefruit liqueur','pamplemousse rose liqueur'],
                'substitutions': ['brandy']}

ingredient_dict['passion fruit liqueur'] = {'category':'liqueur',
                'search_terms': ['alizé red passion','alizé gold passion','passion-fruit liqueur','passion fruit liqueur'],
                'substitutions': []}

ingredient_dict['honey liqueur'] = {'category':'liqueur',
                'search_terms': ['honey liqueur','nonino gioiello'],
                'substitutions': ['drambuie']}

ingredient_dict['coconut liqueur'] = {'category':'liqueur',
                'search_terms': ['coconut liqueur'],
                'substitutions': []}

ingredient_dict['allspice liqueur'] = {'category':'liqueur',
                'search_terms': ['allspice dram','pimento liqueur'],
                'substitutions': []}

ingredient_dict['rose hip liqueur'] = {'category':'liqueur',
                'search_terms': ['rose hip liqueur'],
                'substitutions': []}

ingredient_dict['ginger liqueur'] = {'category':'liqueur',
                'search_terms': ['ginger liqueur'],
                'substitutions': []}

ingredient_dict['suze'] = {'category':'liqueur',
                'search_terms': ['suze'],
                'substitutions': []}

ingredient_dict['pimm\'s'] = {'category':'liqueur',
                'search_terms': ['pimm\'s','pimms'],
                'substitutions': []}

ingredient_dict['ouzo'] = {'category':'liqueur',
                'search_terms': ['ouzo'],
                'substitutions': ['sambuca','pastis','arak','pernod','richard','pacharán']}

ingredient_dict['campari'] = {'category':'liqueur',
                'search_terms': ['campari','gran classico bitter','luxardo bitter'],
                'substitutions': ['aperol']}

ingredient_dict['aperol'] = {'category':'liqueur',
                'search_terms': ['aperol'],
                'substitutions': ['campari']}

ingredient_dict['midori'] = {'category':'liqueur',
                'search_terms': ['midori'],
                'substitutions': []}

ingredient_dict['fernet'] = {'category':'liqueur',
                'search_terms': ['fernet'],
                'substitutions': ['cynar','campari','amaro']}

ingredient_dict['strega'] = {'category':'liqueur',
                'search_terms': ['strega'],
                'substitutions': ['yellow chartreuse','génépy des alpes']}

ingredient_dict['cynar'] = {'category':'liqueur',
                'search_terms': ['cynar'],
                'substitutions': ['fernet','campari','amaro']}

ingredient_dict['amaro'] = {'category':'liqueur',
                'search_terms': ['amaro','cardamaro','zwack'],
                'substitutions': ['fernet','campari','cynar']}

ingredient_dict['st. germain'] = {'category':'liqueur',
                'search_terms': ['st. germain','elderflower','st-germain'],
                'substitutions': []}

ingredient_dict['limoncello'] = {'category':'liqueur',
                'search_terms': ['limoncello'],
                'substitutions': []}

ingredient_dict['jagermeister'] = {'category':'liqueur',
                'search_terms': ['jagermeister'],
                'substitutions': ['fernet','campari','cynar','amaro']}

ingredient_dict['picon'] = {'category':'liqueur',
                'search_terms': ['picon','amer picon'],
                'substitutions': ['amaro']}

ingredient_dict['pernod'] = {'category':'liqueur',
                'search_terms': ['pernod','anisette'],
                'substitutions': ['sambuca','pastis','arak','ouzo','richard','pacharán']}

ingredient_dict['arak'] = {'category':'liqueur',
                'search_terms': ['arak'],
                'substitutions': ['sambuca','pastis','ouzo','pernod','richard','pacharán']}

ingredient_dict['sambuca'] = {'category':'liqueur',
                'search_terms': ['sambuca'],
                'substitutions': ['ouzo','pastis','arak','pernod','richard','pacharán']}

ingredient_dict['pastis'] = {'category':'liqueur',
                'search_terms': ['pastis'],
                'substitutions': ['sambuca','ouzo','arak','pernod','richard','pacharán']}

ingredient_dict['pacharán'] = {'category':'liqueur',
                'search_terms': ['pacharán','patxaran'],
                'substitutions': ['sambuca','pastis','arak','pernod','richard','ouzo']}

ingredient_dict['becherovka'] = {'category':'liqueur',
                'search_terms': ['becherovka'],
                'substitutions': []}

ingredient_dict['pine liqueur'] = {'category':'liqueur',
                'search_terms': ['pine liqueur'],
                'substitutions': []}

ingredient_dict['bénédictine'] = {'category':'liqueur',
                'search_terms': ['bénédictine'],
                'substitutions': []}

ingredient_dict['yellow chartreuse'] = {'category':'liqueur',
                'search_terms': ['yellow chartreuse'],
                'substitutions': ['génépy des alpes','strega','bénédictine']}

ingredient_dict['génépy des alpes'] = {'category':'liqueur',
                'search_terms': ['génépy des alpes'],
                'substitutions': ['green chartreuse']}

ingredient_dict['green chartreuse'] = {'category':'liqueur',
                'search_terms': ['green chartreuse'],
                'substitutions': ['génépy des alpes']}


# JUICE:
ingredient_dict['lime juice'] = {'category':'juice',
                'search_terms': ['lime juice'],
                'substitutions': ['lemon juice']}

ingredient_dict['lemon juice'] = {'category':'juice',
                'search_terms': ['lemon juice'],
                'substitutions': ['lime juice']}

ingredient_dict['orange juice'] = {'category':'juice',
                'search_terms': ['orange juice'],
                'substitutions': ['apple juice','pineapple juice','lemonade']}

ingredient_dict['lemonade'] = {'category':'juice',
                'search_terms': ['lemonade'],
                'substitutions': []}

ingredient_dict['pineapple juice'] = {'category':'juice',
                'search_terms': ['pineapple juice'],
                'substitutions': ['orange juice','guava juice','passion fruit juice']}

ingredient_dict['guava juice'] = {'category':'juice',
                'search_terms': ['guava juice'],
                'substitutions': ['pineapple juice','passion fruit juice']}

ingredient_dict['passion fruit juice'] = {'category':'juice',
                'search_terms': ['passion fruit juice'],
                'substitutions': ['pineapple juice','guava juice']}

ingredient_dict['celery juice'] = {'category':'juice',
                'search_terms': ['celery juice'],
                'substitutions': []}

ingredient_dict['cranberry juice'] = {'category':'juice',
                'search_terms': ['cranberry juice'],
                'substitutions': ['grape juice']}

ingredient_dict['pomegranate juice'] = {'category':'juice',
                'search_terms': ['pomegranate juice'],
                'substitutions': []}

ingredient_dict['tangerine juice'] = {'category':'juice',
                'search_terms': ['tangerine juice'],
                'substitutions': ['orange juice']}

ingredient_dict['cantaloupe juice'] = {'category':'juice',
                'search_terms': ['cantaloupe juice'],
                'substitutions': []}

ingredient_dict['watermelon juice'] = {'category':'juice',
                'search_terms': ['watermelon juice'],
                'substitutions': []}

ingredient_dict['apple juice'] = {'category':'juice',
                'search_terms': ['apple cider','apple juice','sparkling cider'],
                'substitutions': []}

ingredient_dict['pear juice'] = {'category':'juice',
                'search_terms': ['pear cider','pear juice'],
                'substitutions': []}

ingredient_dict['carrot juice'] = {'category':'juice',
                'search_terms': ['carrot juice'],
                'substitutions': []}

ingredient_dict['grape juice'] = {'category':'juice',
                'search_terms': ['grape juice','verjus blanc'],
                'substitutions': []}

ingredient_dict['grapefruit juice'] = {'category':'juice',
                'search_terms': ['grapefruit juice'],
                'substitutions': []}

ingredient_dict['tomato juice'] = {'category':'juice',
                'search_terms': ['tomato juice'],
                'substitutions': ['sangrita']}

ingredient_dict['clam juice'] = {'category':'juice',
                'search_terms': ['clam juice','clamato'],
                'substitutions': ['sangrita']}

ingredient_dict['shrub'] = {'category':'juice',
                'search_terms': ['quince shrub','concord shrub'],
                'substitutions': []}

ingredient_dict['sangrita'] = {'category':'juice',
                'search_terms': ['sangrita'],
                'substitutions': ['tomato juice'],
                'instructions': 'https://en.wikipedia.org/wiki/Sangrita'}

# MIXES:
ingredient_dict['bergerac mix'] = {'category':'mix',
                'search_terms': ['bergerac mix'],
                'substitutions': [],
                'instructions': 'https://www.cocktaillove.com/ingredients/bergerac-mix-death-co/'}

ingredient_dict['pendennis mix'] = {'category':'mix',
                'search_terms': ['pendennis mix'],
                'substitutions': [],
                'instructions': 'https://www.cocktaillove.com/ingredients/death-co-pendennis-mix/'}

ingredient_dict['zombie mix'] = {'category':'mix',
                'search_terms': ['zombie mix'],
                'substitutions': [],
                'instructions': 'https://www.cocktaillove.com/ingredients/death-co-zombie-mix/'}

ingredient_dict['donn\'s spices'] = {'category':'mix',
                'search_terms': ['donn\'s spices'],
                'substitutions': [],
                'instructions': 'https://www.cocktaillove.com/ingredients/death-co-dons-spices-2/'}

ingredient_dict['donn\'s mix'] = {'category':'mix',
                'search_terms': ['donn\'s mix'],
                'substitutions': [],
                'instructions': 'https://www.cocktaillove.com/ingredients/donns-mix-1/'}



# SODA:
ingredient_dict['ginger soda'] = {'category':'soda',
                'search_terms': ['ginger ale','ginger soda','ginger beer'],
                'substitutions': ['soda water']}

ingredient_dict['soda water'] = {'category':'soda',
                'search_terms': ['soda water','club soda'],
                'substitutions': []}

ingredient_dict['tonic water'] = {'category':'soda',
                'search_terms': ['tonic water'],
                'substitutions': []}

ingredient_dict['lemon soda'] = {'category':'soda',
                'search_terms': ['lemon soda','7-up','sprite','limonata'],
                'substitutions': ['soda water','grapefruit soda']}

ingredient_dict['coca-cola'] = {'category':'soda',
                'search_terms': ['coca-cola'],
                'substitutions': []}

ingredient_dict['grapefruit soda'] = {'category':'soda',
                'search_terms': ['grapefruit soda'],
                'substitutions': ['soda water','lemon soda']}

# SYRUP:
ingredient_dict['simple syrup'] = {'category':'syrup',
                'search_terms': ['simple syrup','demerara','cane sugar syrup','rich syrup'],
                'substitutions': []}

ingredient_dict['grenadine'] = {'category':'syrup',
                'search_terms': ['grenadine','pomegranate molasses'],
                'substitutions': ['simple syrup']}

ingredient_dict['tonic syrup'] = {'category':'syrup',
                'search_terms': ['tonic syrup'],
                'substitutions': []}

ingredient_dict['raspberry syrup'] = {'category':'syrup',
                'search_terms': ['raspberry syrup'],
                'substitutions': ['simple syrup']}

ingredient_dict['gum syrup'] = {'category':'syrup',
                'search_terms': ['gum syrup'],
                'substitutions': ['simple syrup']}

ingredient_dict['cumin syrup'] = {'category':'syrup',
                'search_terms': ['cumin syrup'],
                'substitutions': ['simple syrup']}

ingredient_dict['rose syrup'] = {'category':'syrup',
                'search_terms': ['rose syrup'],
                'substitutions': ['simple syrup']}

ingredient_dict['vanilla syrup'] = {'category':'syrup',
                'search_terms': ['vanilla syrup'],
                'substitutions': ['simple syrup']}

ingredient_dict['cinnamon bark syrup'] = {'category':'syrup',
                'search_terms': ['cinnamon bark syrup'],
                'substitutions': ['simple syrup']}

ingredient_dict['honey syrup'] = {'category':'syrup',
                'search_terms': ['honey syrup','honey'],
                'substitutions': ['agave syrup','simple syrup']}

ingredient_dict['orgeat'] = {'category':'syrup',
                'search_terms': ['orgeat'],
                'substitutions': []}

ingredient_dict['rice syrup'] = {'category':'syrup',
                'search_terms': ['rice syrup'],
                'substitutions': ['simple syrup']}

ingredient_dict['agave syrup'] = {'category':'syrup',
                'search_terms': ['agave syrup','agave nectar'],
                'substitutions': ['honey syrup']}

ingredient_dict['maple syrup'] = {'category':'syrup',
                'search_terms': ['maple syrup'],
                'substitutions': ['simple syrup']}

ingredient_dict['ginger syrup'] = {'category':'syrup',
                'search_terms': ['ginger syrup'],
                'substitutions': ['simple syrup']}

ingredient_dict['lemongrass syrup'] = {'category':'syrup',
                'search_terms': ['lemongrass syrup'],
                'substitutions': ['simple syrup']}

ingredient_dict['apple syrup'] = {'category':'syrup',
                'search_terms': ['apple syrup'],
                'substitutions': ['simple syrup']}

ingredient_dict['hibiscus syrup'] = {'category':'syrup',
                'search_terms': ['hibiscus syrup'],
                'substitutions': ['simple syrup']}

ingredient_dict['passion fruit syrup'] = {'category':'syrup',
                'search_terms': ['passion fruit syrup'],
                'substitutions': ['simple syrup']}

ingredient_dict['scarlet glow syrup'] = {'category':'syrup',
                'search_terms': ['scarlet glow syrup'],
                'substitutions': ['simple syrup'],
                'instructions': 'https://www.cocktaillove.com/ingredients/death-co-scarlet-glow-syrup/'}


# OTHER:
ingredient_dict['egg'] = {'category':'other',
                'search_terms': ['egg white','egg yolk','egg'],
                'substitutions': []}

ingredient_dict['beer'] = {'category':'other',
                'search_terms': ['stout','beer','lager','ale','ipa','pilsner'],
                'substitutions': []}

ingredient_dict['ketchup'] = {'category':'other',
                'search_terms': ['ketchup'],
                'substitutions': []}

ingredient_dict['mustard'] = {'category':'other',
                'search_terms': ['mustard'],
                'substitutions': []}

ingredient_dict['jam'] = {'category':'other',
                'search_terms': ['marmalade','jam','mixed-berry','apricot preserves','raspberry preserves'],
                'substitutions': []}

ingredient_dict['spiced sorrel'] = {'category':'other',
                'search_terms': ['spiced sorrel'],
                'substitutions': []}

ingredient_dict['broth'] = {'category':'other',
                'search_terms': ['beef broth','chicken broth','beef stock','chicken stock'],
                'substitutions': []}

ingredient_dict['vinegar'] = {'category':'other',
                'search_terms': ['rice vinegar','malt vinegar','balsamic vinegar','pickled ramp brine'],
                'substitutions': []}

ingredient_dict['coffee'] = {'category':'other',
                'search_terms': ['coffee','espresso'],
                'substitutions': []}

ingredient_dict['tea'] = {'category':'other',
                'search_terms': ['tea'],
                'substitutions': []}

ingredient_dict['hot sauce'] = {'category':'other',
                'search_terms': ['tabasco','habanero sauce','hot sauce'],
                'substitutions': []}

ingredient_dict['soy sauce'] = {'category':'other',
                'search_terms': ['soy sauce'],
                'substitutions': []}

ingredient_dict['worcestershire'] = {'category':'other',
                'search_terms': ['worcestershire'],
                'substitutions': []}

ingredient_dict['cocoa powder'] = {'category':'other',
                'search_terms': ['cocoa powder'],
                'substitutions': []}

ingredient_dict['heavy cream'] = {'category':'other',
                'search_terms': ['heavy cream','half-and-half'],
                'substitutions': ['milk']}

ingredient_dict['coconut milk'] = {'category':'other',
                'search_terms': ['coconut milk','coco lopez','cream of coconut'],
                'substitutions': ['milk','heavy cream']}

ingredient_dict['yogurt'] = {'category':'other',
                'search_terms': ['yogurt'],
                'substitutions': ['heavy cream']}

ingredient_dict['milk'] = {'category':'other',
                'search_terms': ['milk'],
                'substitutions': []}

ingredient_dict['horchata'] = {'category':'other',
                'search_terms': ['horchata'],
                'substitutions': ['milk']}

ingredient_dict['ice cream'] = {'category':'other',
                'search_terms': ['ice cream','caribbean cream'],
                'substitutions': []}

ingredient_dict['whipped cream'] = {'category':'other',
                'search_terms': ['whipped cream'],
                'substitutions': []}

ingredient_dict['coconut sorbet'] = {'category':'other',
                'search_terms': ['coconut sorbet'],
                'substitutions': []}

ingredient_dict['butter'] = {'category':'other',
                'search_terms': ['vanilla butter','butter','pumpkin butter'],
                'substitutions': []}

ingredient_dict['wasabi'] = {'category':'other',
                'search_terms': ['wasabi','horseradish'],
                'substitutions': []}

ingredient_dict['acid phosphate'] = {'category':'other',
                'search_terms': ['acid phosphate'],
                'substitutions': []}

ingredient_dict['fruits'] = {'category':'other',
                'search_terms': ['wedges','wedge','slices','slice',\
             'piece orange','peel','quartered',\
            'crescent of orange','grapes',\
            'concord grape','chopped canteloupe',\
            'cherries','bananas',\
            'honeydew melon',\
            'wheel','wheels','blueberries','anjou pear','bartlett pear',\
            'peeled tangerine','macerated cranberry','olive'],
                'substitutions': []}

ingredient_dict['purées'] = {'category':'other',
                'search_terms': ['pumpkin purée','kalamansi purée','passion fruit purée','tropical fruit purée',\
           'pear purée','rhubarb purée','peach purée','tamarind purée'],
                'substitutions': []}





# WINE: 
ingredient_dict['port'] = {'category':'wine',
                'search_terms': ['port','madeira'],
                'substitutions': ['dry vermouth','sweet vermouth']}

ingredient_dict['sake'] = {'category':'wine',
                'search_terms': ['sake'],
                'substitutions': ['dry vermouth','sweet vermouth']}



ingredient_dict['dry vermouth'] = {'category':'wine',
                'search_terms': ['dry vermouth'],
                'substitutions': ['sake','white wine','sherry','lillet blanc','cocchi americano']}

ingredient_dict['cocchi americano'] = {'category':'wine',
                'search_terms': ['cocchi americano','gentiane aperitif'],
                'substitutions': ['lillet blanc','sherry','dry vermouth']}

ingredient_dict['sweet vermouth'] = {'category':'wine',
                'search_terms': ['sweet vermouth','punt e mes','gentiane-quina','antica formula'],
                'substitutions': ['port']}

ingredient_dict['sherry'] = {'category':'wine',
                'search_terms': ['sherry'],
                'substitutions': ['port','dry vermouth','sweet vermouth']}

ingredient_dict['lilet blanc'] = {'category':'wine',
                'search_terms': ['lillet blanc','lille blanc'],
                'substitutions': ['dry vermouth','cocchi americano']}

ingredient_dict['lilet rouge'] = {'category':'wine',
                'search_terms': ['lillet rouge','red dubonnet','dubonnet rouge','saint-raphaël apértif'],
                'substitutions': ['dry vermouth']}

ingredient_dict['red wine'] = {'category':'wine',
                'search_terms': ['red wine','rioja','cabernet','beaujolais'],
                'substitutions': []}

ingredient_dict['white wine'] = {'category':'wine',
                'search_terms': ['white wine','chardonnay','rosé','savignon blanc','sauvignon blanc','riesling'],
                'substitutions': []}

ingredient_dict['champagne'] = {'category':'wine',
                'search_terms': ['champagne','prosecco'],
                'substitutions': []}

ingredient_dict['dessert wine'] = {'category':'wine',
                'search_terms': ['dessert wine','tokaji','drouhin pommeau','ice wine'],
                'substitutions': ['port']}


# BITTERS
ingredient_dict['orange flower water'] = {'category':'bitters',
                'search_terms': ['orange flower water'],
                'substitutions': []}

ingredient_dict['angostura'] = {'category':'bitters',
                'search_terms': ['angostura'],
                'substitutions': ['orange bitters']} # can expand here

ingredient_dict['celery bitters'] = {'category':'bitters',
                'search_terms': ['celery bitters'],
                'substitutions': []} # can expand here

ingredient_dict['habanero bitters'] = {'category':'bitters',
                'search_terms': ['habanero bitters'],
                'substitutions': []} # can expand here

ingredient_dict['goldenseal tincture'] = {'category':'bitters',
                'search_terms': ['goldenseal tincture'],
                'substitutions': []} # can expand here

ingredient_dict['tobacco essence'] = {'category':'bitters',
                'search_terms': ['tobacco essence'],
                'substitutions': []} # can expand here


# GARNISH
ingredient_dict['garnish'] = {'category':'garnish',
                'search_terms': ['garnish','cracked ice','grapefruit peel','stalk of celery','ice','asparagus','coin of grapefruit','maggi'],
                'substitutions': []}

# SPICES and HERBS
ingredient_dict['salt'] = {'category':'spices and herbs',
                'search_terms': ['salt'],
                'substitutions': []}

ingredient_dict['pepper'] = {'category':'spices and herbs',
                'search_terms': ['pepper','peppercorn'],
                'substitutions': []}

ingredient_dict['clove'] = {'category':'spices and herbs',
                'search_terms': ['clove','cloves'],
                'substitutions': []}

ingredient_dict['nutmeg'] = {'category':'spices and herbs',
                'search_terms': ['nutmeg'],
                'substitutions': []}

ingredient_dict['cardamom'] = {'category':'spices and herbs',
                'search_terms': ['cardamom'],
                'substitutions': []}

ingredient_dict['sugar'] = {'category':'spices and herbs',
                'search_terms': ['sugar'],
                'substitutions': []}

ingredient_dict['oregano'] = {'category':'spices and herbs',
                'search_terms': ['oregano'],
                'substitutions': []}

ingredient_dict['dill'] = {'category':'spices and herbs',
                'search_terms': ['dill'],
                'substitutions': []}

ingredient_dict['mint'] = {'category':'spices and herbs',
                'search_terms': ['mint'],
                'substitutions': []}

ingredient_dict['basil'] = {'category':'spices and herbs',
                'search_terms': ['basil'],
                'substitutions': []}

ingredient_dict['rosemary'] = {'category':'spices and herbs',
                'search_terms': ['rosemary'],
                'substitutions': []}

ingredient_dict['sage'] = {'category':'spices and herbs',
                'search_terms': ['sage'],
                'substitutions': []}

ingredient_dict['shiso'] = {'category':'spices and herbs',
                'search_terms': ['shiso'],
                'substitutions': []}

ingredient_dict['curry leaf'] = {'category':'spices and herbs',
                'search_terms': ['curry leaf'],
                'substitutions': []}



# Search term list:
# search_terms = [item for key in ingredient_dict.keys() for item in ingredient_dict.get(key).get('search_terms')]


measure_list = ['ounce','ounces','oz','dash','dashes','part','parts','teaspoon',\
                 'teaspoons','tablespoons','tablespoon','pinch','barspoon',
                 'drop','drops','wineglass','bottle','cup','float',\
                 'liqueur glass','pony','pint','pints','splash','lump','cube']


measure_dict = {'ounce':1, # unit with multipliers for ounce transform
               'ounces':1,
                'oz':1,
                'oz.':1,
                'dash':0.02,
                'dashes':0.02,
                'part':1,
                'parts':1,
                'teaspoon':0.167,
                'tsp':0.167,
                'teaspoons':0.167,
                'tablespoon':0.5,
                'tbs.':0.5,
                'tablespoons':0.5,
                'pinch':0.01,
                'barspoon':0.035,
                'drop':0.002,
                'drops':0.002,
                'wineglass':5,
                'bottle':8, # guessing
                'cup':8,
                'float':0.5,
                'liqueur glass':1.5,
                'pony':1,
                'pint':16,
                'pints':16,
                'splash':0.5,
                'lump':0.27, # based on simple syrup
                'cube':0.27
               }
