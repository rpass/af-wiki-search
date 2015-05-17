from bs4 import BeautifulSoup
import bleach
import urllib


def get_htmlSource(url):
	#url += "?action=render" #may be a bad idea
	sock = urllib.urlopen(url)
	htmlSource = sock.read()
	sock.close()

	#htmlSource = bleach.clean(htmlSource, strip=True)
	return htmlSource

def get_htmlText(text):
	soup = BeautifulSoup(text)
	# text = soup.get_text()
	links = soup.find(id="mw-content-text").find('a')
	text = soup.find(id="mw-content-text").get_text()
	text += soup.find(id="catlinks").get_text()
	text = bleach.clean(text, strip=True)

	title = soup.find(id="firstHeading").get_text()

	return text.encode('utf-8'), title.encode('utf-8'), links

def savedoc(text, filename):
	filename = "docs/" + filename
	f = open(filename, 'w')
	f.write(text) # TODO: Check if unicode is important
	f.close()

def get_dochrefs(url):
	# returns list of urls on a page
	text = 
	soup = BeautifulSoup()
	return 0

def bfs(start):
	# returns list of related urls
	# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
	visited = set()
	queue = get_dochrefs(start)
	while queue and len(visited) < MINDOCCOUNT:
		vertex = queue.pop()
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(get_dochrefs(vertex))
	return visited




MINDOCLENGTH = 750 #words
MINDOCCOUNT = 4 #documents
doc_count = 0
docURL = "http://af.wikipedia.org/wiki/Spesiaal:Lukraak"

while doc_count < MINDOCCOUNT:
	html = get_htmlSource(docURL)
	text, docTitle = get_htmlText(html)
	# test
	print(' '.join((docTitle, str(doc_count))))

	# Check if doc meets our length requirements.
	# Save if yes, try again if not
	words = text.split(" ")
	# test
	if len(words) >= MINDOCLENGTH:
		doc_count += 1
		savedoc(text, docTitle)
