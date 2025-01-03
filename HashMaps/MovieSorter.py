from flask import Flask, request, jsonify, render_template,redirect,url_for
import NewHashMap as mapper
import json
import atexit


app = Flask(__name__)

movieBank = mapper.NewHashMap()

def load_movieBank():
    try:
        with open('movieBankMovies.json', 'r') as file:
            info = json.load(file)
            movieBank.from_dict(info)
    except FileNotFoundError:
        pass

load_movieBank()

def save_movieBank():
    with open('movieBankMovies.json', 'w') as file:
        json.dump(movieBank.to_dict(), file)


atexit.register(save_movieBank)


@app.route('/')
def home():
    return render_template('index.html')    

@app.route('/add', methods=['POST', 'GET'])
def add_movie():
    if request.method == "POST":
        title = request.form['title']
        director = request.form['director']
        year = request.form['year']
        rating = request.form['rating']

        if title and year and rating and director:
            # "Stored" signifies that the movie title has been successfully added to the movieBank
            movieBank[title] = {
                'director': director,
                'year': int(year),
                'rating': int(rating)
            }
            return redirect(url_for('listed_movies'))
    return render_template('add_movie.html', error="Title is required.")
    
@app.route('/list')
def listed_movies():
    movie_list = {key: movieBank[key] for key in movieBank}
    return render_template('listed_movies.html', movieBank=movie_list)

@app.route("/search", methods=["POST", "GET"])
def search_movie():
    result = None

    if request.method == "POST":
        title = request.form['title']
        if title and movieBank.contains(title):
            result = f"'{title}' is in the collection."
        else:
            result = f"'{title}' is not in the collection."
    return render_template('search_movie.html', result=result)

@app.route('/delete', methods=['POST'])
def delete_movie():
    result = None

    while request.method == "POST":
        title = request.form['title']
        if title and movieBank.contains(title):
            movieBank.__delitem__(title)
            result = f"'{title}' has been deleted."
        else:
            result = f"'{title}' is not in the collection."
    return render_template('delete_movie.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
    