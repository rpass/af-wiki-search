AF-wiki-search
Information Retrieval Project
UCT Computer Science Honours 2015

Authors:
Rob Passmore
Lauren Sanby

This is an academic project to build a search engine that returns relevant results when queried in afrikaans.
We are 'indexing' 535 afrikaans wikipedia articles as our document collection and enforcing a minimum document length of ±750 words to increase quality of results.

----

To Run:

This web application uses Python 2.7 to run a webserver.

Dependencies:

	Python 2.7
	Flask (sudo pip install flask)


----

TODO:

Get webserver to send correct GET requests to SOLR
Get webserver to receive returned results from SOLR
Get webserver to extract links from JSON returned by SOLR
Get webserver to format results page correctly

