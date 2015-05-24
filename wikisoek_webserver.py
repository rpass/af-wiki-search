from flask import Flask, render_template, request
import cgi
import re

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
	query = request.form['query']
	query = query.strip()

	# Remove all non-word characters (everything except numbers and letters)
	query = re.sub(r"[^\w\s]", '', query)
	# Replace whitespace with + for SOLR query
	query = query.replace(' ', '+')

	if (query == ""):
		return render_template('index.html')
	else:

	# "http://localhost:8983/solr/IRSELR/select?q="+query+"&wt=python&indent=true&hl=true&hl.simple.pre=%3Cem%3E&hl.simple.post=%3C%2Fem%3E&hl.highlightMultiTerm=true"
	# "http://localhost:8983/solr/IRSELR/select?q="+query+"&wt=python&indent=true"
	# send GET request to SOLR

		results = ["result 1", "result 2", "result 3"]
		query = query.replace('+', ' ')
		return render_template('results.html', query = query, results = results)

# @app.route('/reviews/<int:movie_id>/')
# def getreview(movie_id):
# 	moviename = session.query(Movie).filter_by(id=movie_id).one().name
# 	review = session.query(Review).filter_by(movieId=movie_id).one()
# 	output = '<h2>%s</h2></br>'%moviename
# 	output += '%s</br>'%(review.reviewText)
# 	return output

# @app.route('/reviews/<int:movie_id>/edit/')
# def editreview(movie_id):
# 	return "editing movie: %s"%movie_id

# @app.route('/reviews/<int:movie_id>/delete/')
# def deletereview(movie_id):
# 	return "deleting movie: %s"%movie_id

# @app.route('/reviews/new/', methods=['GET', 'POST'])
# def createreview():
# 	if(request.method == 'POST'):
# 		print 'posting new review'

			
# 		moviename = request.form['moviename']
# 		moviereview = request.form['moviereview']

# 		newmovie = Movie(name=moviename, year=2012)
# 		session.add(newmovie)
# 		session.commit()

# 		newreview = Review(reviewText=moviereview, friendsList='Rob, Natasha', movie=newmovie)
# 		session.add(newreview)
# 		session.commit()

# 		return HelloWorld()
# 	else:
# 		return render_template('newreview.html')


if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port=5000)