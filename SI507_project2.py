# Import flask and classes
from flask import Flask
from movies_tools import Movie
import random

# Set-up application
app = Flask(__name__)

# Routes
@app.route('/')
def basic():
    f = open("movies_clean.csv", 'r')
    lines = f.readlines()
    f.close()

    num_movies = len(lines)
    return '<h1>{} movies recorded.</h1>'.format(num_movies)

@app.route('/movies/ratings')
def home():
    f = open("movies_clean.csv", 'r')
    lines = f.readlines()
    f.close()

    # Create empty string of movies to be added onto
    movies_str = ""

    random.shuffle(lines)
    for i in range(5):
        movie_inst = Movie(lines[i])
        movies_str += movie_inst.__str__()

    return movies_str

if __name__ == "__main__":
    app.run()
