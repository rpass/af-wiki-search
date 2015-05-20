from bs4 import BeautifulSoup
import bleach
import urllib
import re
from collections import deque


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
	# links = soup.find(id="mw-content-text").find('a')
	text = soup.find(id="mw-content-text").get_text()
	text += soup.find(id="catlinks").get_text()
	text = bleach.clean(text, strip=True)

	title = soup.find(id="firstHeading").get_text()

	return text.encode('utf-8'), title.encode('utf-8')

def savedoc(text, filename):
	filename = "docs/" + filename
	try:
		
		f = open(filename, 'w')
		f.write(text) # TODO: Check if unicode is important
		f.close()
	except Exception, e:
		pass


def get_dochrefs(url):
	# returns list of urls on a page
	sock = urllib.urlopen(url)
	text = sock.read()
	sock.close()

	soup = BeautifulSoup(text)
	alist = soup.body.find(id="mw-content-text").find_all('a')
	# create list of links by retrieving the value to the 'href' key in each element of the alist
	links = []

	p = re.compile(r"/wiki/")

	for a in alist:
		href = a['href']
		if p.match(href):
			links.append(''.join(("http://af.wikipedia.org",href)))
	# print("$$$$$$$$$$$ Links: %s"%links)

	return links

def bfs(start):
	# returns list of related urls
	# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
	visited = []
	queue = deque(get_dochrefs(start))

	# for x in queue: print("%s\n"%x)
	while queue and len(visited) < MINDOCCOUNT:
		vertex = queue.popleft()
		if vertex not in visited:
			visited.append(vertex)
			print("vertex: %s, %s"%((vertex,str(len(visited)))))
			queue.extend(get_dochrefs(vertex))
			# print("vertex: %s"%vertex)
	return visited


if __name__ == "__main__":

	MINDOCLENGTH = 300 #words
	MINDOCCOUNT = 1000 #documents
	doc_count = 0
	# startURL = "http://af.wikipedia.org/wiki/Spesiaal:Lukraak"
	startURL = "http://af.wikipedia.org/wiki/Lys_van_politieke_partye_in_Suid-Afrika"
	url_list = bfs(startURL)

	for url in url_list:
		html = get_htmlSource(url)
		text, docTitle = get_htmlText(html)
		# test
		#print(' '.join((docTitle, str(doc_count))))

		# Check if doc meets our length requirements.
		# Save if yes, try again if not
		words = text.split(" ")
		# test
		if len(words) >= MINDOCLENGTH:
			doc_count += 1
			savedoc(text, docTitle)
			if doc_count%10 == 0:
				print("%s,%s"%((docTitle, doc_count)))


	# while doc_count < MINDOCCOUNT:
	# 	html = get_htmlSource(startURL)
	# 	text, docTitle = get_htmlText(html)
	# 	# test
	# 	print(' '.join((docTitle, str(doc_count))))

	# 	# Check if doc meets our length requirements.
	# 	# Save if yes, try again if not
	# 	words = text.split(" ")
	# 	# test
	# 	if len(words) >= MINDOCLENGTH:
	# 		doc_count += 1
	# 		savedoc(text, docTitle)
