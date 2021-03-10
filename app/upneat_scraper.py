# Scrapes upneat.rocks for all recipes from PDT, Death&Co, and Craft of the Cocktail
# dumps data into raw_drinks.pickle

import pickle
import requests
from bs4 import BeautifulSoup
from time import sleep


def scrape_cocktail(url): # Scrapes each cocktail
	base_url = "http://www.upneat.rocks"
	response = requests.get(f"{base_url}{url}")
	soup = BeautifulSoup(response.text, "html.parser")
	cocktail_info = soup.find(class_="col-md-12 col-lg-5")
	p_tag = cocktail_info.find_all(["p"])
	ingredients = cocktail_info.find(["ul"]).get_text().splitlines()
	ingredients = list(filter(None,ingredients))
	if len(p_tag)==1:
		instructions = ''
	else:
		instructions = p_tag[1].get_text()
	if len(p_tag) >2:
		comments = p_tag[2].get_text()
	else:
		comments = ''
	cocktail_title = cocktail_info.find(["h3"]).get_text().splitlines()[1]
	print(f"scraping {cocktail_title}")
	source = cocktail_info.find(["h3"]).get_text().splitlines()[4]
	d = {
		"cocktail_name": cocktail_title, 
		"ingredients": ingredients, 
		"instructions":instructions,
		"comments":comments,
		"source":source}
	return d


def scrape_source(url): # Scrapes each source on upneat.rocks
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	cocktail_soup = soup.find_all(class_="col-xs-12 col-md-6 col-lg-3")
	cocktail_list = []
	for cocktail in cocktail_soup: # loop through all cocktails here to get urls:
		a_tag = cocktail.find_all("a")
		cocktail_url = a_tag[0]['href'] # call scrape_cocktail here
		d = scrape_cocktail(cocktail_url)
		cocktail_list.append(d)
		sleep(.8)
	return cocktail_list


# Go through and complile three books:
master_list = []
cocktail_list = scrape_source("http://www.upneat.rocks/recipe/sources/the-craft-of-the-cocktail")
master_list.append(cocktail_list)
cocktail_list = scrape_source("http://www.upneat.rocks/recipe/sources/death-co")
master_list.append(cocktail_list)
cocktail_list = scrape_source("http://www.upneat.rocks/recipe/sources/pdt")
master_list.append(cocktail_list)

# Pickle:
with open("raw_drinks.pickle", "wb") as file:
	pickle.dump(master_list, file)
