AF-wiki-search
Information Retrieval Project
UCT Computer Science Honours 2015

Authors:
Rob Passmore
Lauren Sanby

This is an academic project to build a search engine that returns relevant results when queried in afrikaans.
We are 'indexing' 1,000 afrikaans wikipedia articles as our document collection and enforcing a minimum document length of ±750 words to increase quality of results.

----

TODO:

First step
Collect documents

	Currently we can fetch any number of random documents from af.wikipedia.org. fetchdocs.py strips the content from the webpages and creates a doc for each page. Now we need to fetch related docs. I have constructed a Breadth-First Search function bfs that takes a starting url and generates a list of related urls by following the links on each page in a breadth first fashion. BFS is chosen to collect the documents most closely linked to the original document first, and then go for more indirectly linked documents.

	Still needs to be done: write a function that fetches all the hrefs from a documents content.
	Then the program needs to be run to fetch roughly 1,000 docs. 

Create testing queries

