from flask import Flask, request, jsonify, render_template, redirect, url_for
import NewHashMap as mapper
import json
import atexit

app = Flask(__name__)

movieBank = mapper.NewHashMap()

def load_movieBank():
    try:
        with open("movieBankMovies.json", "r") as file:
            info = json.load(file)
            print("Movie Data:", info)
            movieBank.from_dict(info)
    except FileNotFoundError:
        print("No movie data found.")
        pass

load_movieBank()

def save_movieBank():
    with open("movieBankMovies.json", "w") as file:
        json.dump(movieBank.to_dict(), file)
        movieBank.__repr__()

atexit.register(save_movieBank)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST', 'GET'])
def add_movie():
    if request.method == "POST":
        title = request.form.get('title')
        director = request.form.get('director')
        year = request.form.get('year')
        rating = request.form.get('rating')

        if all([title, director, year, rating]):
            try:
                year = int(year)
                rating = int(rating)
                movieBank[title] = {
                    'director': director,
                    'year': year,
                    'rating': rating
                }
                return redirect(url_for('listed_movies'))
            except ValueError:
                return render_template('add_movie.html', error="Year and Rating must be integers.")
        else:
            return render_template('add_movie.html', error="All fields are required.")
    return render_template('add_movie.html')

@app.route('/list')
def listed_movies():
    movie_list = movieBank.to_dict()
    print("Current Movie Bank:  ",movie_list)
    return render_template('listed_movies.html', movieBank=movie_list)

@app.route('/update', methods=['POST', 'GET'])
def update_movie():
    result = None

    if request.method == "POST":
        title = request.form.get('title')
        new_director = request.form.get('director')
        new_year = request.form.get('year')
        new_rating = request.form.get('rating')

        if all(title):
            try:
                if movieBank.contains(title):
                    movie = movieBank[title]

                    if new_director:
                        movie['director'] = new_director

                    if new_year:
                        try:
                            movie['year'] = int(new_year)
                        except ValueError:
                            return render_template('update_movie.html', error="Year must be an integer.")
                        
                    if new_rating:
                        try:
                            movie['rating'] = int(new_rating)
                        except ValueError:  
                            return render_template('update_movie.html', error="Rating must be an integer.")
                    
                    movieBank[title] = movie
                    result = f"'{title}' has been updated."

            except KeyError:
                result = f"'{title}' is not in the collection."

        else:
            result = "All fields are required."
    
    return render_template('update_movie.html', result=result)

@app.route("/search", methods=["POST", "GET"])
def search_movie():
    result = None
    if request.method == "POST":
        title = request.form.get('title')
        if title:
            if movieBank.contains(title):
                result = f"'{title}' is in the collection."
            else:
                result = f"'{title}' is not in the collection."
        else:
            result = "Title is required."
    return render_template('search_movie.html', result=result)

@app.route('/delete', methods=['POST', 'GET'])
def delete_movie():
    result = None
    if request.method == "POST":
        title = request.form.get('title')
        if title:
            if movieBank.contains(title):
                movieBank.__delitem__(title)
                result = f"'{title}' has been deleted."
            else:
                result = f"'{title}' is not in the collection."
        else:
            result = "Title is required."
    return render_template('delete_movie.html', result=result)

if __name__ == "__main__":
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(debug=debug_mode)