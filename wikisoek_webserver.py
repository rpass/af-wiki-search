from flask import Flask, render_template, request
import cgi

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
	query = request.form['query']

	# send GET request to SOLR
	results = ["result 1", "result 2", "result 3"]
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