from bs4 import BeautifulSoup
import urllib


def get_htmlSource(url):
	url += "?action=render"
	sock = urllib.urlopen(url)
	htmlSource = sock.read()
	sock.close()
	return htmlSource

def get_htmlText(text):
	soup = BeautifulSoup(text)
	text = soup.get_text()
	title = soup.title.string
	return text.encode('utf-8'), title

def savedoc(text, filename):
	filename = "docs/" + filename
	f = open(filename, 'w')
	f.write(text) # TODO: Check if unicode is important
	f.close()


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
	print (words)
	if len(words) >= MINDOCLENGTH:
		doc_count += 1
		savedoc(text, docTitle)
