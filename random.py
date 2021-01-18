import wikipedia
import webbrowser

count = int(input("How many pages (1-10)? : "))


pages = wikipedia.random(pages=count)

try:
	for page in pages:
		webbrowser.open(wikipedia.page(page).url)
except wikipedia.exceptions.PageError:
	pass