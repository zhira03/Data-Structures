import json

def checkImageKey(movieInfo, movieTitle):
    return "image" in movieInfo[movieTitle]

def add_image_to_Title(movieBankPath, imageURLs):
    try:
        with open(movieBankPath, "r") as file:
            movieInfo = json.load(file)

        url_index = 0

        for movieTitle in movieInfo:
            if not checkImageKey(movieInfo, movieTitle):
                if url_index < len(imageURLs):
                    movieInfo[movieTitle]["image"] = imageURLs[url_index]
                    url_index += 1
                else:
                    print("Not enough URLs to add to all movies.")
        
        with open(movieBankPath, "w") as file:
            json.dump(movieInfo, file, indent=4)
        print("Images added to movie titles.")

    except FileNotFoundError:
        print("No movie data found.")
    except json.JSONDecodeError:
        print("Can't Decode JSON data.")
    except Exception as e:
        print("An error occurred:", e)


