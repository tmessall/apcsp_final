import requests
from bs4 import *

def recommend_movies(genre):
	list_genres = ["action/adventure", "animation", "international", "classics", "comedy", "documentary", 
	"drama", "horror", "musical/dance", "mystery", "romance", "sci-fi/fantasy", "sports", "western"]

	is_genre = False
	for i in range(0, len(list_genres)):
		if genre.lower() == list_genres[i]:
			is_genre = True
	if is_genre == False:
		print "Sorry, that isn't a valid genre. Try one of these:"
		print list_genres 

	web_list = ["https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/", 
				"https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/",
				"https://www.rottentomatoes.com/top/bestofrt/top_100_art_house__international_movies/",
				"https://www.rottentomatoes.com/top/bestofrt/top_100_classics_movies/",
				"https://www.rottentomatoes.com/top/bestofrt/top_100_comedy_movies/",
				"https://www.rottentomatoes.com/top/bestofrt/top_100_documentary_movies/",
				"https://www.rottentomatoes.com/top/bestofrt/top_100_drama_movies/",
				"https://www.rottentomatoes.com/top/bestofrt/top_100_horror_movies/",
				"https://www.rottentomatoes.com/top/bestofrt/top_100_musical__performing_arts_movies/",
				"https://www.rottentomatoes.com/top/bestofrt/top_100_mystery__suspense_movies/",
				"https://www.rottentomatoes.com/top/bestofrt/top_100_romance_movies/",
				"https://www.rottentomatoes.com/top/bestofrt/top_100_science_fiction__fantasy_movies/",
				"https://www.rottentomatoes.com/top/bestofrt/top_100_sports__fitness_movies/",
				"https://www.rottentomatoes.com/top/bestofrt/top_100_western_movies/"]

	for i in range(0, len(list_genres)):
		if genre == list_genres[i]:
			top_in_genre = get_page(web_list[i])
			movie_titles = search_inside_html(top_in_genre, 'tr', '', 'a')
			display_list(movie_titles[1:6])

def search_inside_html(html, element, class_name, inner_element):
	soup = BeautifulSoup(html, "html.parser")
	elements = soup.findAll(element, {"class": class_name})

	results = []
	for element in elements:
		results.append(element.find(inner_element))

	return results

def get_page(url):
	req = requests.get(url)
	return req.text.encode('utf-8')

def display_list(elements):
	for element in elements:
		display(element)

def display(element):
	print element.string.encode('utf-8')

prompt = "> "

print "What is your favorite genre?"
ans = raw_input(prompt)

recommend_movies(ans)