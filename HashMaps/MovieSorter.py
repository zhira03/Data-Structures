from flask import Flask, request, jsonify, render_template,redirect,url_for
import NewHashMap as mapper

app = Flask(__name__)

movieBank = mapper.NewHashMap()

@app.route('/')
def home():
    return render_template('index.html')    

@app.route('/add', methods=['POST', 'GET'])
def add_movie():
    if request.method == "POST":
        title = request.form['title']
        if title:
            # "Stored" signifies that the movie title has been successfully added to the movieBank
            movieBank[title] = "Stored"
            return redirect(url_for('listed_movies'))
    return render_template('add_movie.html', error="Title is required.")
    
@app.route('/list')
def listed_movies():
    movie_list = list(movieBank)
    return render_template('listed_movies.html', movieBank=movie_list)

@app.route("/search", methods=["POST", "GET"])
def search_movie():
    result = None

    while request.method == "POST":
        title = request.form['title']
        if title and movieBank.contains(title):
            result = f"'{title}' is in the collection."
        else:
            result = f"'{title}' is not in the collection."
    return render_template('search_movie', result=result)

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
    