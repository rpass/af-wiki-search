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

	Currently we have a rudimentary wikipedia scraper but it is in need of improvement. Currently it grabs everything in between the 'body' tags of the webpage. This is not accurate enough and we must implement python's bleach library to ignore the non-content related elements (eg. <script>).

Create testing queries

